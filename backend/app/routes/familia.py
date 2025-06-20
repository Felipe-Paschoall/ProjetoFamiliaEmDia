from flask import Blueprint, request, session, redirect, url_for, render_template, current_app, flash
from werkzeug.security import generate_password_hash
from .auth import admin_required, login_required
import time

bp = Blueprint('familia', __name__, url_prefix='/familia')

@bp.route('/create', methods=['GET', 'POST'])
def create_family():
    if request.method == 'POST':
        familia_nome = request.form['family_name']
        nome_admin = request.form['nome']
        cpf = request.form['cpf']
        senha = request.form['password']
        
        db = current_app.get_db()
        error = None
        
        if not familia_nome:
            error = 'Nome da família é obrigatório.'
        elif not nome_admin:
            error = 'Nome do administrador é obrigatório.'
        elif not cpf:
            error = 'CPF é obrigatório.'
        elif not senha:
            error = 'Senha é obrigatória.'
        elif len(senha) < 6:
            error = 'A senha deve ter pelo menos 6 caracteres.'
            
        if error is None:
            try:
                # Cria família
                cur = db.execute('INSERT INTO familia (nome) VALUES (?)',
                               (familia_nome,))
                familia_id = cur.lastrowid
                
                # Cria usuário administrador
                senha_hash = generate_password_hash(senha)
                db.execute('''
                    INSERT INTO usuario (familia_id, nome, cpf, password, is_admin, first_login)
                    VALUES (?, ?, ?, ?, 1, 0)
                ''', (familia_id, nome_admin, cpf, senha_hash))
                db.commit()
                
                return redirect(url_for('auth.login'))
            except db.IntegrityError:
                error = 'CPF já cadastrado.'
                
        flash(error)
        
    return render_template('familia/create.html')

@bp.route('/list_members')
@login_required
def list_members():
    db = current_app.get_db()
    members = db.execute('''
        SELECT id, nome, cpf, is_admin, first_login
        FROM usuario
        WHERE familia_id = ?
    ''', (session['family_id'],)).fetchall()
    
    return render_template('familia/members.html', members=members)

@bp.route('/members/new', methods=['GET', 'POST'])
@admin_required
def add_member():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        is_admin = 1 if request.form.get('is_admin') == 'on' else 0
        db = current_app.get_db()
        error = None
        if not nome:
            error = 'Nome é obrigatório.'
        elif not cpf:
            error = 'CPF é obrigatório.'
        if error is None:
            try:
                senha_padrao = generate_password_hash('senha123')
                db.execute('''
                    INSERT INTO usuario (familia_id, nome, cpf, password, is_admin, first_login)
                    VALUES (?, ?, ?, ?, ?, 1)
                ''', (session['family_id'], nome, cpf, senha_padrao, is_admin))
                db.commit()
                return redirect(url_for('familia.list_members'))
            except db.IntegrityError:
                error = 'CPF já cadastrado.'
        flash(error)
    return render_template('familia/add_member.html')

@bp.route('/members/<int:id>/delete', methods=['POST'])
@admin_required
def delete_member(id):
    db = current_app.get_db()
    # Não pode remover a si mesmo
    if id == session.get('user_id'):
        flash('Você não pode remover a si mesmo.', 'error')
        return redirect(url_for('familia.list_members'))
    member = db.execute('SELECT * FROM usuario WHERE id = ? AND familia_id = ?',
                       (id, session['family_id'])).fetchone()
    if member is None:
        flash('Membro não encontrado.')
    else:
        # Invalidar todas as sessões ativas do usuário
        db.execute('''
            CREATE TABLE IF NOT EXISTS sessoes_invalidas (
                user_id INTEGER PRIMARY KEY,
                invalidated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.execute('INSERT OR REPLACE INTO sessoes_invalidas (user_id) VALUES (?)', (id,))
        db.commit()
        
        # Remover o usuário
        db.execute('DELETE FROM usuario WHERE id = ?', (id,))
        db.commit()
        flash('Membro excluído com sucesso.')
    return redirect(url_for('familia.list_members'))

@bp.route('/members/<int:id>/toggle-admin', methods=['POST'])
@admin_required
def toggle_admin(id):
    db = current_app.get_db()
    # Não pode alterar a si mesmo
    if id == session.get('user_id'):
        flash('Você não pode alterar seu próprio status de administrador.', 'error')
        return redirect(url_for('familia.list_members'))
    member = db.execute('SELECT * FROM usuario WHERE id = ? AND familia_id = ?',
                       (id, session['family_id'])).fetchone()
    if member is None:
        flash('Membro não encontrado.', 'error')
    else:
        novo_status = 0 if member['is_admin'] else 1
        db.execute('UPDATE usuario SET is_admin = ? WHERE id = ?', (novo_status, id))
        db.commit()
        if novo_status:
            flash('Usuário promovido a administrador com sucesso!', 'success')
        else:
            flash('Permissão de administrador removida com sucesso!', 'success')
        # Sinalizar para o usuário afetado que ele deve ser deslogado
        db.execute('UPDATE usuario SET first_login = 2 WHERE id = ?', (id,))
        db.commit()
    return redirect(url_for('familia.list_members'))

@bp.route('/profile/edit', methods=['GET', 'POST'])
@admin_required
def edit_profile():
    db = current_app.get_db()
    user = db.execute('SELECT * FROM usuario WHERE id = ?', (session['user_id'],)).fetchone()
    
    if request.method == 'POST':
        novo_nome = request.form.get('novo_nome')
        error = None
        
        if not novo_nome:
            error = 'O novo nome é obrigatório.'
            
        if error is None:
            db.execute('UPDATE usuario SET nome = ? WHERE id = ?', 
                      (novo_nome, session['user_id']))
            db.commit()
            # Atualizar o nome na sessão para refletir no header
            session['user_nome'] = novo_nome
            flash('Nome atualizado com sucesso!', 'success')
            return redirect(url_for('familia.list_members'))
            
        flash(error, 'error')
    
    return render_template('familia/edit_profile.html', user=user) 
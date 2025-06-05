from flask import Blueprint, request, session, redirect, url_for, render_template, current_app, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .auth import login_required, admin_required
import json

bp = Blueprint('solicitacoes', __name__, url_prefix='/solicitacoes')

@bp.route('/')
@login_required
def list_requests():
    db = current_app.get_db()
    
    if session.get('is_admin'):
        # Admin vê todas as solicitações da família
        solicitacoes = db.execute('''
            SELECT s.*, u.nome as solicitante_nome
            FROM solicitacao s
            JOIN usuario u ON s.usuario_id = u.id
            WHERE u.familia_id = ?
            ORDER BY s.created_at DESC
        ''', (session['family_id'],)).fetchall()
    else:
        # Usuário vê apenas suas solicitações
        solicitacoes = db.execute('''
            SELECT s.*, u.nome as solicitante_nome
            FROM solicitacao s
            JOIN usuario u ON s.usuario_id = u.id
            WHERE s.usuario_id = ?
            ORDER BY s.created_at DESC
        ''', (session['user_id'],)).fetchall()
    
    return render_template('solicitacoes/list.html', solicitacoes=solicitacoes)

@bp.route('/create', methods=['POST'])
@login_required
def create_request():
    tipo = request.form.get('tipo')
    senha_atual = request.form.get('senha_atual')
    
    if not senha_atual:
        flash('A senha atual é obrigatória.', 'error')
        return redirect(url_for('familia.list_members'))
    
    # Verifica a senha atual
    db = current_app.get_db()
    user = db.execute('SELECT * FROM usuario WHERE id = ?', 
                     (session['user_id'],)).fetchone()
    
    if not check_password_hash(user['password'], senha_atual):
        flash('Senha atual incorreta.', 'error')
        return redirect(url_for('familia.list_members'))
    
    if tipo == 'alteracao_nome':
        novo_nome = request.form.get('novo_nome')
        if not novo_nome:
            flash('O novo nome é obrigatório.', 'error')
            return redirect(url_for('familia.list_members'))
        
        detalhes = {'novo_nome': novo_nome}
    else:
        flash('Tipo de solicitação inválido.', 'error')
        return redirect(url_for('familia.list_members'))
    
    db.execute('''
        INSERT INTO solicitacao (usuario_id, tipo, detalhes)
        VALUES (?, ?, ?)
    ''', (session['user_id'], tipo, json.dumps(detalhes)))
    db.commit()
    
    flash('Solicitação enviada com sucesso! Aguarde a aprovação do administrador.', 'success')
    return redirect(url_for('familia.list_members'))

@bp.route('/<int:id>/approve', methods=['POST'])
@admin_required
def approve_request(id):
    db = current_app.get_db()
    
    # Verifica se a solicitação pertence à família do admin
    solicitacao = db.execute('''
        SELECT s.*, u.id as user_id
        FROM solicitacao s
        JOIN usuario u ON s.usuario_id = u.id
        WHERE s.id = ? AND u.familia_id = ?
    ''', (id, session['family_id'])).fetchone()
    
    if solicitacao is None:
        flash('Solicitação não encontrada.')
        return redirect(url_for('solicitacoes.list_requests'))
    
    detalhes = json.loads(solicitacao['detalhes'])
    
    if solicitacao['tipo'] == 'alteracao_nome':
        db.execute(
            'UPDATE usuario SET nome = ? WHERE id = ?',
            (detalhes['novo_nome'], solicitacao['user_id'])
        )
    
    db.execute(
        "UPDATE solicitacao SET status = 'aprovado' WHERE id = ?",
        (id,)
    )
    db.commit()
    
    flash('Solicitação aprovada com sucesso.')
    return redirect(url_for('solicitacoes.list_requests'))

@bp.route('/<int:id>/reject', methods=['POST'])
@admin_required
def reject_request(id):
    db = current_app.get_db()
    
    # Verifica se a solicitação pertence à família do admin
    solicitacao = db.execute('''
        SELECT s.*
        FROM solicitacao s
        JOIN usuario u ON s.usuario_id = u.id
        WHERE s.id = ? AND u.familia_id = ?
    ''', (id, session['family_id'])).fetchone()
    
    if solicitacao is None:
        flash('Solicitação não encontrada.')
    else:
        db.execute(
            "UPDATE solicitacao SET status = 'rejeitado' WHERE id = ?",
            (id,)
        )
        db.commit()
        flash('Solicitação rejeitada.')
    
    return redirect(url_for('solicitacoes.list_requests')) 
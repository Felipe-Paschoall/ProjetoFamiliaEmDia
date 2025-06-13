from flask import Blueprint, request, session, redirect, url_for, render_template, current_app, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

bp = Blueprint('auth', __name__, url_prefix='/auth')

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
            
        db = current_app.get_db()
        
        # Verificar se a sessão foi invalidada (usuário removido)
        sessao_invalida = db.execute(
            'SELECT 1 FROM sessoes_invalidas WHERE user_id = ?', 
            (session['user_id'],)
        ).fetchone()
        
        if sessao_invalida:
            session.clear()
            flash('Sua conta foi removida da família. Contate um administrador.', 'error')
            return redirect(url_for('auth.login'))
            
        # Verificar alteração de status de admin
        user = db.execute('SELECT first_login FROM usuario WHERE id = ?', 
                         (session['user_id'],)).fetchone()
        if user is None:  # Usuário não existe mais
            session.clear()
            flash('Sua conta foi removida da família. Contate um administrador.', 'error')
            return redirect(url_for('auth.login'))
            
        if user and user['first_login'] == 2:  # Status de admin alterado
            user_id = session['user_id']
            session.clear()
            flash('Seu status de administrador foi alterado. Faça login novamente.', 'warning')
            db.execute('UPDATE usuario SET first_login = 0 WHERE id = ?', (user_id,))
            db.commit()
            return redirect(url_for('auth.login'))
            
        return view(*args, **kwargs)
    return wrapped_view

def admin_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not session.get('is_admin'):
            return redirect(url_for('auth.login'))
        return view(*args, **kwargs)
    return wrapped_view

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cpf = request.form['cpf']
        senha = request.form['password']
        db = current_app.get_db()
        
        error = None
        user = db.execute('SELECT * FROM usuario WHERE cpf = ?', (cpf,)).fetchone()
        
        if user is None:
            error = 'Credenciais inválidas.'
        elif user['first_login'] and senha != 'senha123':
            error = 'No primeiro acesso, use a senha padrão: senha123'
        elif not user['first_login'] and not check_password_hash(user['password'], senha):
            error = 'Credenciais inválidas.'
            
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            session['family_id'] = user['familia_id']
            session['is_admin'] = bool(user['is_admin'])
            session['first_login'] = bool(user['first_login'])
            session['user_nome'] = user['nome']
            
            if user['first_login']:
                return redirect(url_for('auth.change_password'))
                
            return redirect(url_for('familia.list_members'))
            
        flash(error)
        
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

@bp.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        is_first_login = session.get('first_login', False)
        
        if not is_first_login:
            senha_atual = request.form['current_password']
            if not senha_atual:
                flash('A senha atual é obrigatória.', 'error')
                return render_template('auth/change_password.html')
        
        nova_senha = request.form['new_password']
        confirma_senha = request.form['confirm_password']
        
        db = current_app.get_db()
        error = None
        
        user = db.execute('SELECT * FROM usuario WHERE id = ?', 
                         (session['user_id'],)).fetchone()
        
        if not is_first_login and not check_password_hash(user['password'], senha_atual):
            error = 'Senha atual incorreta.'
        elif nova_senha != confirma_senha:
            error = 'As novas senhas não coincidem.'
        elif len(nova_senha) < 6:
            error = 'A nova senha deve ter pelo menos 6 caracteres.'
            
        if error is None:
            db.execute(
                'UPDATE usuario SET password = ?, first_login = 0 WHERE id = ?',
                (generate_password_hash(nova_senha), session['user_id'])
            )
            db.commit()
            
            if is_first_login:
                session['first_login'] = False
                flash('Senha alterada com sucesso! Bem-vindo ao sistema!', 'success')
            else:
                flash('Senha alterada com sucesso!', 'success')
                
            return redirect(url_for('familia.list_members'))
            
        flash(error, 'error')
        
    return render_template('auth/change_password.html')

@bp.route('/about')
def about():
    return render_template('auth/about.html') 
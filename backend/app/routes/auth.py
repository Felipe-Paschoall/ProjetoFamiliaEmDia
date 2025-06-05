from flask import Blueprint, request, session, redirect, url_for, render_template, current_app, flash
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

bp = Blueprint('auth', __name__, url_prefix='/auth')

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if 'user_id' not in session:
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
            error = 'CPF não encontrado.'
        elif not check_password_hash(user['password'], senha):
            error = 'Senha incorreta.'
            
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            session['family_id'] = user['familia_id']
            session['is_admin'] = bool(user['is_admin'])
            session['first_login'] = bool(user['first_login'])
            
            if user['first_login']:
                return redirect(url_for('auth.change_password'))
                
            return redirect(url_for('tarefas.list_tasks'))
            
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
        senha_atual = request.form['senha_atual']
        nova_senha = request.form['nova_senha']
        confirma_senha = request.form['confirma_senha']
        
        db = current_app.get_db()
        error = None
        
        user = db.execute('SELECT * FROM usuario WHERE id = ?', 
                         (session['user_id'],)).fetchone()
        
        if not check_password_hash(user['password'], senha_atual):
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
            flash('Senha alterada com sucesso!', 'success')
            return redirect(url_for('familia.list_members'))
            
        flash(error, 'error')
        
    return redirect(url_for('familia.list_members')) 
from flask import Blueprint, redirect, url_for, render_template, session, current_app, flash
from .auth import login_required
import os

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('tarefas.list_tasks'))
    return redirect(url_for('auth.login'))

@bp.route('/init-db')
def init_db():
    """Inicializa o banco de dados."""
    try:
        db = current_app.get_db()
        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
        flash('Banco de dados inicializado com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao inicializar banco de dados: {str(e)}', 'error')
    
    return redirect(url_for('auth.login'))

@bp.route('/load-test-data')
def load_test_data():
    """Carrega dados de teste no banco de dados."""
    try:
        db = current_app.get_db()
        # Primeiro inicializa o banco
        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))
        # Depois carrega os dados de teste
        with current_app.open_resource('dados_familias.sql') as f:
            db.executescript(f.read().decode('utf8'))
        flash('Dados de teste carregados com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao carregar dados de teste: {str(e)}', 'error')
    
    return redirect(url_for('auth.login')) 
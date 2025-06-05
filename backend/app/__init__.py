from flask import Flask
from flask_session import Session
from config import config
import sqlite3
from flask import g
from datetime import datetime
import os
import json

def create_app(config_name='default'):
    app = Flask(__name__, instance_relative_config=True)
    
    # Carrega configurações
    app.config.from_object(config[config_name])
    
    # Inicializa extensões
    Session(app)
    
    # Função para obter conexão com o banco
    def get_db():
        if 'db' not in g:
            g.db = sqlite3.connect(app.config['DATABASE'])
            g.db.row_factory = sqlite3.Row
        return g.db

    # Fecha conexão com o banco ao fim da requisição
    @app.teardown_appcontext
    def close_db(error):
        if hasattr(g, 'db'):
            g.db.close()
    
    # Registra as blueprints
    from .routes import auth, familia, tarefas, solicitacoes, main
    app.register_blueprint(auth.bp)
    app.register_blueprint(familia.bp)
    app.register_blueprint(tarefas.bp)
    app.register_blueprint(solicitacoes.bp)
    app.register_blueprint(main.bp)
    
    # Registra função get_db no contexto da aplicação
    app.get_db = get_db
    
    # Registra filtro para formatar datas
    @app.template_filter('datetime')
    def format_datetime(value):
        if value is None:
            return ""
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                return value
        return value.strftime('%d/%m/%Y %H:%M')

    @app.template_filter('from_json')
    def from_json(value):
        return json.loads(value) if value else {}
    
    return app 
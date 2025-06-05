import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    # Configuração básica
    SECRET_KEY = os.getenv('SECRET_KEY', 'chave-secreta-para-desenvolvimento')
    
    # Configuração do banco de dados
    DATABASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'BancoDeDados', 'familia.db')
    
    # Configuração da sessão
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 1800  # 30 minutos

class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    DEBUG = False

# Dicionário com as configurações disponíveis
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
} 
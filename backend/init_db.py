import sqlite3
import os

def init_db():
    # Obtém o caminho do banco de dados
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'BancoDeDados', 'familia.db')
    
    # Obtém o caminho do schema (agora da pasta app)
    schema_path = os.path.join(os.path.dirname(__file__), 'app', 'schema.sql')
    
    # Remove o banco de dados se ele existir
    if os.path.exists(db_path):
        os.remove(db_path)
    
    # Lê o schema
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema = f.read()
    
    # Conecta ao banco de dados
    conn = sqlite3.connect(db_path)
    
    try:
        # Executa o schema
        conn.executescript(schema)
        conn.commit()
        print("Banco de dados inicializado com sucesso!")
        
        # Verifica se as tabelas foram criadas
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        print("\nTabelas criadas:")
        for table in tables:
            print(f"- {table[0]}")
            
    except sqlite3.Error as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    init_db() 
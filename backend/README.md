# Backend - Família em Dia

Este diretório contém a API em Flask (Python) do projeto Família em Dia.

## Tecnologias

- Python 3.x
- Flask 3.0.2
- SQLite (via SQLAlchemy)
- Flask-Session 0.6.0 para autenticação
- python-dotenv 1.0.1 para variáveis de ambiente
- Werkzeug 3.0.1

## Estrutura do Projeto

```
backend/
├── app/
│   ├── __init__.py          # Configuração principal da aplicação
│   ├── routes/              # Rotas da API
│   ├── static/              # Arquivos estáticos
│   ├── templates/           # Templates HTML
│   └── schema.sql           # Schema do banco de dados
├── config.py                # Configurações da aplicação
├── init_db.py              # Script de inicialização do banco
├── requirements.txt        # Dependências do projeto
└── run.py                  # Script de execução
```

## Endpoints da API

### Autenticação

- `POST /auth/login`: Login do usuário
- `POST /auth/logout`: Logout do usuário
- `POST /auth/change-password`: Alteração de senha

### Família

- `GET /familia`: Detalhes da família
- `POST /familia`: Criar nova família
- `PUT /familia`: Atualizar dados da família

### Usuários

- `GET /usuarios`: Listar usuários da família
- `POST /usuarios`: Adicionar novo usuário
- `PUT /usuarios/<id>`: Atualizar usuário
- `DELETE /usuarios/<id>`: Remover usuário

### Tarefas

- `GET /tarefas`: Listar tarefas
- `POST /tarefas`: Criar nova tarefa
- `PUT /tarefas/<id>`: Atualizar tarefa
- `DELETE /tarefas/<id>`: Remover tarefa
- `PUT /tarefas/<id>/status`: Atualizar status

### Solicitações

- `GET /solicitacoes`: Listar solicitações
- `POST /solicitacoes`: Criar solicitação
- `PUT /solicitacoes/<id>/status`: Aprovar/rejeitar solicitação

## Configuração do Ambiente

1. Criar arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=sua_chave_secreta
```

2. Criar ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instalar dependências:

```bash
pip install -r requirements.txt
```

4. Inicializar o banco de dados:

```bash
python init_db.py
```

5. Executar o servidor:

```bash
python run.py
```

## Desenvolvimento

- O servidor será executado em `http://localhost:5000`
- Logs de desenvolvimento são exibidos no console
- O banco de dados SQLite é criado automaticamente na primeira execução

## Segurança

- Todas as senhas são armazenadas com hash
- Sessões são gerenciadas via Flask-Session
- Autenticação é requerida para todas as rotas exceto login
- CSRF protection está habilitada

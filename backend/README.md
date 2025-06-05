# Backend - Família em Dia

Este diretório contém a API em Flask (Python) do projeto Família em Dia.

## Tecnologias

- Python
- Flask
- SQLite (via SQLAlchemy)
- Flask-Session para autenticação

## Estrutura Planejada

```
backend/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── familia.py
│   │   ├── usuario.py
│   │   ├── tarefa.py
│   │   └── solicitacao.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── familia.py
│   │   ├── tarefas.py
│   │   └── solicitacoes.py
│   └── utils/
│       ├── __init__.py
│       └── auth_helpers.py
├── config.py
└── requirements.txt
```

## Endpoints Planejados

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

## Como Executar (Futuro)

1. Criar ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Instalar dependências:

```bash
pip install -r requirements.txt
```

3. Executar servidor de desenvolvimento:

```bash
flask run
```

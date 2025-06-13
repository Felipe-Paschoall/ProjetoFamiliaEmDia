# Projeto Família em Dia

Sistema web para gerenciamento de tarefas em família, desenvolvido como projeto educacional.

## Estrutura do Projeto

O projeto está dividido em duas partes principais:

1. **[BancoDeDados](./BancoDeDados/README.md)**

   - SQLite como banco de dados
   - Schema com tabelas para famílias, usuários, tarefas e solicitações
   - Scripts SQL para criação e manutenção do banco

2. **[Backend](./backend/README.md)**

   - API REST em Flask (Python)
   - Interface web integrada (HTML/CSS/JavaScript)
   - Autenticação por sessão
   - Endpoints para gerenciamento de famílias, usuários, tarefas e solicitações

## Tecnologias Utilizadas

- **Banco de Dados**: SQLite
- **Backend**: Python 3.x + Flask 3.0.2
- **Frontend**: HTML + CSS + JavaScript (Vanilla)
- **Autenticação**: Flask-Session 0.6.0
- **Outras Dependências**:
  - Werkzeug 3.0.1
  - python-dotenv 1.0.1

## Funcionalidades Principais

1. **Gestão de Famílias**

   - Criação de família
   - Adição/remoção de membros
   - Perfis de administrador e usuário comum

2. **Gestão de Tarefas**

   - Criação, edição e remoção de tarefas
   - Atribuição de responsáveis
   - Acompanhamento de status
   - Agendamento opcional

3. **Sistema de Solicitações**

   - Pedidos de alteração de dados
   - Aprovação/rejeição por administradores
   - Histórico de solicitações

4. **Autenticação e Segurança**
   - Login com CPF e senha
   - Troca obrigatória de senha no primeiro acesso
   - Controle de permissões por perfil

## Como Executar

1. **Pré-requisitos**

   - Python 3.8 ou superior
   - SQLite3
   - Git (opcional, para clonar o repositório)

2. **Configurar o Ambiente**

   ```bash
   # Clone o repositório (se ainda não tiver feito)
   git clone [URL_DO_REPOSITÓRIO]
   cd ProjetoFamiliaEmDia

   # Crie e ative o ambiente virtual
   python -m venv venv
   venv\Scripts\activate

   # Instale as dependências do Python
   pip install -r backend/requirements.txt
   ```

3. **Configurar Variáveis de Ambiente**

   ```bash
   # Crie um arquivo .env na raiz do projeto com:
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=sua_chave_secreta
   ```

4. **Configurar o Banco de Dados**

   ```bash
   # Navegue até a pasta do backend
   cd backend

   # Execute o script de inicialização do banco de dados
   python init_db.py
   ```

   Você deve ver a mensagem "Banco de dados inicializado com sucesso!" e a lista de tabelas criadas.

5. **Executar o Projeto**

   ```bash
   # Execute o servidor
   python run.py
   ```

   O servidor iniciará automaticamente:

   - Backend API: http://localhost:5000
   - Interface Web: http://localhost:5000 (servida pelo próprio backend)

6. **Acessar o Sistema**
   - Abra seu navegador e acesse http://localhost:5000
   - Como é uma instalação nova, você precisará:
     1. Criar uma nova família
     2. Registrar um usuário administrador
     3. Começar a usar o sistema

## Estrutura de Diretórios

```
ProjetoFamiliaEmDia/
├── BancoDeDados/        # Banco de dados
│   ├── schema.sql
│   └── familia.db
├── backend/            # API REST e Interface Web
│   ├── app/
│   │   ├── static/     # Arquivos estáticos (CSS, JS)
│   │   ├── templates/  # Templates HTML
│   │   └── routes/     # Rotas da API
│   ├── config.py
│   ├── init_db.py
│   └── run.py
├── venv/              # Ambiente virtual Python
└── .env              # Variáveis de ambiente
```

## Solução de Problemas Comuns

1. **Erro "no such table"**

   - Se você encontrar o erro "no such table", execute novamente o script de inicialização:
     ```bash
     cd backend
     python init_db.py
     ```
   - Verifique se o arquivo `BancoDeDados/familia.db` existe e tem tamanho maior que 0 bytes

2. **Erro de permissão**

   - Certifique-se de que você tem permissões de escrita na pasta do projeto
   - No Windows, execute o PowerShell como administrador se necessário
   - Verifique se o arquivo `BancoDeDados/familia.db` não está aberto em outro programa

3. **Erro de porta em uso**

   - Se a porta 5000 estiver em uso, você pode alterar a porta no arquivo `backend/run.py`
   - Procure a linha `app.run(host='0.0.0.0', port=5000)` e altere o número da porta

4. **Erro de dependências**
   - Se encontrar erros relacionados a pacotes Python, tente reinstalar as dependências:
     ```bash
     pip uninstall -r backend/requirements.txt -y
     pip install -r backend/requirements.txt
     ```

## Licença

Este projeto é para fins educacionais.

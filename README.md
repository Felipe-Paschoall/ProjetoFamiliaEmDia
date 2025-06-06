# Projeto Família em Dia

Sistema web para gerenciamento de tarefas em família, desenvolvido como projeto educacional.

## Estrutura do Projeto

O projeto está dividido em três partes principais:

1. **[BancoDeDados](./BancoDeDados/README.md)**

   - SQLite como banco de dados
   - Schema com tabelas para famílias, usuários, tarefas e solicitações
   - Scripts SQL para criação e manutenção do banco

2. **[Backend](./backend/README.md)**

   - API REST em Flask (Python)
   - Autenticação por sessão
   - Endpoints para gerenciamento de famílias, usuários, tarefas e solicitações

3. **[Frontend](./frontend/README.md)**
   - Interface web em HTML/CSS/JavaScript puro
   - Design responsivo
   - Interface intuitiva para gerenciamento de tarefas

## Tecnologias Utilizadas

- **Banco de Dados**: SQLite
- **Backend**: Python + Flask
- **Frontend**: HTML + CSS + JavaScript (Vanilla)
- **Autenticação**: Flask-Session

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

   # Instale as dependências do Python
   pip install -r backend/requirements.txt
   ```

3. **Configurar o Banco de Dados**
   ```bash
   # Navegue até a pasta do backend
   cd backend

   # Execute o script de inicialização do banco de dados
   python init_db.py
   ```
   Você deve ver a mensagem "Banco de dados inicializado com sucesso!" e a lista de tabelas criadas.

4. **Executar o Projeto**
   ```bash
   # Execute o servidor
   python run.py
   ```

   O servidor iniciará automaticamente:
   - Backend API: http://localhost:5000
   - Frontend: http://localhost:5000 (servido pelo próprio backend)

5. **Acessar o Sistema**
   - Abra seu navegador e acesse http://localhost:5000
   - Como é uma instalação nova, você precisará:
     1. Criar uma nova família
     2. Registrar um usuário administrador
     3. Começar a usar o sistema

**Observações:**
- O frontend é servido automaticamente pelo backend Flask
- O banco de dados SQLite é criado localmente na pasta `BancoDeDados`
- Certifique-se de que a porta 5000 está disponível no seu sistema

**Solução de Problemas Comuns:**

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

## Desenvolvimento

O projeto está organizado de forma modular para facilitar o desenvolvimento e manutenção:

```
ProjetoFamiliaEmDia/
├── BancoDeDados/        # Banco de dados
│   ├── schema.sql
│   └── familia.db
├── backend/            # API REST
│   └── app/
└── frontend/          # Interface web
    ├── css/
    ├── js/
    └── pages/
```

## Contribuição

Este é um projeto educacional desenvolvido como trabalho acadêmico. Contribuições são bem-vindas através de:

1. Fork do repositório
2. Criação de branch para feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit das mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para o branch (`git push origin feature/nova-funcionalidade`)
5. Criação de Pull Request

## Licença

Este projeto é para fins educacionais.

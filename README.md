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

1. **Configurar Banco de Dados**

   - Instalar SQLite3
   - Seguir instruções em [BancoDeDados/README.md](./BancoDeDados/README.md)

2. **Configurar Backend**

   - Instalar Python
   - Seguir instruções em [backend/README.md](./backend/README.md)

3. **Configurar Frontend**
   - Seguir instruções em [frontend/README.md](./frontend/README.md)

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

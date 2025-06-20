# Banco de Dados - Família em Dia

Este diretório contém os arquivos relacionados ao banco de dados SQLite do projeto Família em Dia.

## Estrutura

O banco de dados consiste em 4 tabelas principais:

1. `familia`: Armazena informações das famílias

   - `id`: Identificador único (chave primária)
   - `nome`: Nome da família
   - `created_at`: Data de criação (com ajuste de fuso horário -3 horas)

2. `usuario`: Armazena informações dos membros da família

   - `id`: Identificador único (chave primária)
   - `familia_id`: Referência à família (chave estrangeira)
   - `nome`: Nome do usuário
   - `cpf`: CPF único do usuário
   - `password`: Hash da senha
   - `is_admin`: Indica se é administrador
   - `first_login`: Indica se ainda usa senha padrão
   - `created_at`: Data de criação (com ajuste de fuso horário -3 horas)

3. `tarefa`: Armazena as tarefas da família

   - `id`: Identificador único (chave primária)
   - `familia_id`: Referência à família (chave estrangeira)
   - `criador_id`: ID do usuário que criou a tarefa
   - `destinatario_id`: ID do usuário responsável
   - `titulo`: Título da tarefa
   - `descricao`: Descrição detalhada
   - `horario`: Data/hora opcional (formato: YYYY-MM-DD HH:MM:SS)
   - `status`: Estado da tarefa (pendente, aprovada, rejeitada, atrasada, concluida)
   - `justificativa`: Texto opcional para justificar alterações
   - `created_at`: Data de criação (com ajuste de fuso horário -3 horas)
   - `updated_at`: Data da última atualização

4. `solicitacao`: Armazena solicitações de alteração
   - `id`: Identificador único (chave primária)
   - `usuario_id`: ID do usuário solicitante
   - `tipo`: Tipo da solicitação
   - `detalhes`: Detalhes da solicitação
   - `status`: Estado da solicitação
   - `created_at`: Data de criação (com ajuste de fuso horário -3 horas)
   - `updated_at`: Data da última atualização

## Arquivos

- `schema.sql`: Script SQL com a definição das tabelas
- `familia.db`: Arquivo do banco de dados SQLite

## Como Usar

Para interagir com o banco de dados, você precisa ter o SQLite3 instalado.

### Comandos Básicos

1. Abrir o console do SQLite:

```bash
C:\sqlite3\sqlite3.exe familia.db
```

2. Comandos úteis no console:

- `.tables`: Lista todas as tabelas
- `.schema TABELA`: Mostra a estrutura de uma tabela
- `.quit`: Sai do console

3. Executar o script de criação:

```bash
C:\sqlite3\sqlite3.exe familia.db ".read schema.sql"
```

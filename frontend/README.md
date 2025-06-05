# Frontend - Família em Dia

Este diretório contém a interface web do projeto Família em Dia, desenvolvida com HTML, CSS e JavaScript puro.

## Tecnologias

- HTML5
- CSS3
- JavaScript (Vanilla)
- Fetch API para comunicação com o backend

## Estrutura Planejada

```
frontend/
├── css/
│   ├── style.css
│   └── components/
│       ├── forms.css
│       ├── buttons.css
│       └── cards.css
├── js/
│   ├── api/
│   │   ├── config.js
│   │   ├── auth.js
│   │   ├── familia.js
│   │   ├── tarefas.js
│   │   └── solicitacoes.js
│   ├── components/
│   │   ├── navbar.js
│   │   ├── taskCard.js
│   │   └── modal.js
│   └── utils/
│       ├── auth.js
│       └── validators.js
└── pages/
    ├── index.html
    ├── login.html
    ├── dashboard.html
    ├── tarefas.html
    ├── familia.html
    └── solicitacoes.html
```

## Páginas Principais

1. **Login** (`login.html`)

   - Formulário de login
   - Redefinição de senha no primeiro acesso

2. **Dashboard** (`dashboard.html`)

   - Visão geral das tarefas
   - Notificações
   - Resumo da família

3. **Tarefas** (`tarefas.html`)

   - Lista de tarefas
   - Criação/edição de tarefas
   - Filtros e busca

4. **Família** (`familia.html`)

   - Lista de membros
   - Gerenciamento de membros (admin)
   - Perfil do usuário

5. **Solicitações** (`solicitacoes.html`)
   - Lista de solicitações
   - Aprovação/rejeição (admin)
   - Criação de solicitações

## Funcionalidades Planejadas

- Autenticação de usuários
- Gerenciamento de tarefas
- Notificações em tempo real
- Responsividade para dispositivos móveis
- Temas claro/escuro
- Validações de formulários
- Feedback visual de ações
- Modais de confirmação

## Como Executar (Futuro)

1. Instalar extensão Live Server no VS Code ou similar

2. Clicar com botão direito em `index.html` e selecionar "Open with Live Server"

3. O site abrirá automaticamente no navegador

## Observações

- O frontend será desenvolvido sem frameworks para demonstrar domínio de JavaScript puro
- Foco em UI/UX intuitiva e responsiva
- Implementação de boas práticas de acessibilidade
- Código modular e reutilizável

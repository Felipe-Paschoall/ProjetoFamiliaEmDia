-- Tabela de famílias
CREATE TABLE familia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

-- Tabela de usuários (membros da família)
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    familia_id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    cpf TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT 0,
    first_login BOOLEAN NOT NULL DEFAULT 1,
    FOREIGN KEY (familia_id) REFERENCES familia(id)
);

-- Tabela de tarefas
CREATE TABLE tarefa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    atribuida_para INTEGER NOT NULL,
    criada_por INTEGER NOT NULL,
    horario DATETIME,
    status TEXT NOT NULL DEFAULT 'pendente',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (atribuida_para) REFERENCES usuario(id),
    FOREIGN KEY (criada_por) REFERENCES usuario(id)
);

-- Tabela de solicitações de alteração de dados
CREATE TABLE solicitacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    tipo TEXT NOT NULL,
    detalhes TEXT,
    status TEXT NOT NULL DEFAULT 'pendente',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
); 
DROP TABLE IF EXISTS familia;
DROP TABLE IF EXISTS usuario;
DROP TABLE IF EXISTS tarefa;
DROP TABLE IF EXISTS solicitacao;

CREATE TABLE familia (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT (datetime('now', '-3 hours'))
);

CREATE TABLE usuario (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  familia_id INTEGER NOT NULL,
  nome TEXT NOT NULL,
  cpf TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  is_admin INTEGER NOT NULL DEFAULT 0,
  first_login INTEGER NOT NULL DEFAULT 1,
  created_at TIMESTAMP NOT NULL DEFAULT (datetime('now', '-3 hours')),
  FOREIGN KEY (familia_id) REFERENCES familia (id)
);

CREATE TABLE tarefa (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  familia_id INTEGER NOT NULL,
  criador_id INTEGER NOT NULL,
  destinatario_id INTEGER NOT NULL,
  titulo TEXT NOT NULL,
  descricao TEXT,
  horario DATETIME,
  status TEXT NOT NULL DEFAULT 'pendente',
  created_at TIMESTAMP NOT NULL DEFAULT (datetime('now', '-3 hours')),
  updated_at TIMESTAMP,
  FOREIGN KEY (familia_id) REFERENCES familia (id),
  FOREIGN KEY (criador_id) REFERENCES usuario (id),
  FOREIGN KEY (destinatario_id) REFERENCES usuario (id)
);

CREATE TABLE solicitacao (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  usuario_id INTEGER NOT NULL,
  tipo TEXT NOT NULL,
  detalhes TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'pendente',
  created_at TIMESTAMP NOT NULL DEFAULT (datetime('now', '-3 hours')),
  updated_at TIMESTAMP,
  FOREIGN KEY (usuario_id) REFERENCES usuario (id)
); 
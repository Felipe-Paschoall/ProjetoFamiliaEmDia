-- Inserir família
INSERT INTO familia (nome) VALUES ('Família Silva');

-- Inserir usuários (senha: 123456)
INSERT INTO usuario (familia_id, nome, cpf, password, is_admin) 
VALUES (1, 'João Silva', '123.456.789-00', 'pbkdf2:sha256:600000$dxrFcWAk9q3nGWvp$c9b9a69c7e5c4553f6ef9c3ad0b4d28f3e8e2b03e6e9c2b6c7e4d5f6a3b2c1d0', 1);

INSERT INTO usuario (familia_id, nome, cpf, password) 
VALUES (1, 'Maria Silva', '987.654.321-00', 'pbkdf2:sha256:600000$dxrFcWAk9q3nGWvp$c9b9a69c7e5c4553f6ef9c3ad0b4d28f3e8e2b03e6e9c2b6c7e4d5f6a3b2c1d0');

-- Inserir algumas tarefas
INSERT INTO tarefa (familia_id, criador_id, destinatario_id, titulo, descricao, status)
VALUES 
  (1, 1, 2, 'Lavar a louça', 'Lavar a louça do almoço', 'aprovada'),
  (1, 1, 2, 'Varrer a casa', 'Varrer todos os cômodos', 'pendente'),
  (1, 2, 1, 'Fazer compras', 'Comprar itens da lista do mercado', 'aprovada'); 
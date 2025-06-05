-- Família Santos
INSERT INTO familia (nome) VALUES ('Família Santos');
INSERT INTO usuario (familia_id, nome, cpf, password, is_admin) VALUES 
(1, 'Carlos Santos', '111.222.333-01', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 1),
(1, 'Ana Santos', '111.222.333-02', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 1),
(1, 'Pedro Santos', '111.222.333-03', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(1, 'Julia Santos', '111.222.333-04', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(1, 'Lucas Santos', '111.222.333-05', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(1, 'Mariana Santos', '111.222.333-06', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(1, 'Felipe Santos', '111.222.333-07', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0);

-- Família Oliveira
INSERT INTO familia (nome) VALUES ('Família Oliveira');
INSERT INTO usuario (familia_id, nome, cpf, password, is_admin) VALUES 
(2, 'Roberto Oliveira', '222.333.444-01', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 1),
(2, 'Patricia Oliveira', '222.333.444-02', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 1),
(2, 'Gabriel Oliveira', '222.333.444-03', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(2, 'Beatriz Oliveira', '222.333.444-04', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(2, 'Thiago Oliveira', '222.333.444-05', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0);

-- Família Pereira
INSERT INTO familia (nome) VALUES ('Família Pereira');
INSERT INTO usuario (familia_id, nome, cpf, password, is_admin) VALUES 
(3, 'Marcelo Pereira', '333.444.555-01', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 1),
(3, 'Sandra Pereira', '333.444.555-02', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 1),
(3, 'Ricardo Pereira', '333.444.555-03', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 1),
(3, 'Fernanda Pereira', '333.444.555-04', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(3, 'Diego Pereira', '333.444.555-05', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(3, 'Camila Pereira', '333.444.555-06', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(3, 'Bruno Pereira', '333.444.555-07', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(3, 'Laura Pereira', '333.444.555-08', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(3, 'Rafael Pereira', '333.444.555-09', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(3, 'Isabella Pereira', '333.444.555-10', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0);

-- Família Costa
INSERT INTO familia (nome) VALUES ('Família Costa');
INSERT INTO usuario (familia_id, nome, cpf, password, is_admin) VALUES 
(4, 'Eduardo Costa', '444.555.666-01', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 1),
(4, 'Monica Costa', '444.555.666-02', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 1),
(4, 'Gustavo Costa', '444.555.666-03', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(4, 'Carolina Costa', '444.555.666-04', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(4, 'Henrique Costa', '444.555.666-05', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(4, 'Amanda Costa', '444.555.666-06', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0);

-- Família Lima
INSERT INTO familia (nome) VALUES ('Família Lima');
INSERT INTO usuario (familia_id, nome, cpf, password, is_admin) VALUES 
(5, 'Fernando Lima', '555.666.777-01', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 1),
(5, 'Regina Lima', '555.666.777-02', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 1),
(5, 'Paulo Lima', '555.666.777-03', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 1),
(5, 'Carla Lima', '555.666.777-04', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(5, 'Daniel Lima', '555.666.777-05', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(5, 'Renata Lima', '555.666.777-06', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(5, 'Marcos Lima', '555.666.777-07', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0),
(5, 'Leticia Lima', '555.666.777-08', 'scrypt:32768:8:1$CJFcs03kH6l1fQg7$f70b494d84f2a8a1a5b3d7ddad13d0e82fc294d48011bc453b7d62b45614dc57a66fd2401cf762f5fc2c6c328646f8daefbc1d39f063229a2f8fdcd30e8535fa', 0);

-- Inserir algumas tarefas para cada família
INSERT INTO tarefa (familia_id, criador_id, destinatario_id, titulo, descricao, status) VALUES
-- Família Santos
(1, 1, 3, 'Limpar a garagem', 'Varrer e organizar as ferramentas', 'aprovada'),
(1, 2, 4, 'Lavar roupas', 'Separar por cores e passar', 'pendente'),
(1, 1, 5, 'Cortar grama', 'Aparar o jardim dos fundos', 'concluida'),

-- Família Oliveira
(2, 8, 10, 'Fazer almoço', 'Preparar arroz, feijão e frango', 'aprovada'),
(2, 9, 11, 'Arrumar camas', 'Trocar roupas de cama dos quartos', 'pendente'),
(2, 8, 12, 'Lavar banheiros', 'Limpar os dois banheiros', 'concluida'),

-- Família Pereira
(3, 13, 16, 'Organizar garagem', 'Separar itens para doação', 'aprovada'),
(3, 14, 17, 'Limpar piscina', 'Verificar pH e cloro', 'pendente'),
(3, 15, 18, 'Podar árvores', 'Cortar galhos do jardim', 'rejeitada'),
(3, 13, 19, 'Consertar torneira', 'Trocar vedação da cozinha', 'concluida'),

-- Família Costa
(4, 23, 25, 'Organizar documentos', 'Separar e arquivar contas', 'aprovada'),
(4, 24, 26, 'Limpar janelas', 'Lavar vidros e persianas', 'pendente'),
(4, 23, 27, 'Arrumar jardim', 'Regar plantas e retirar ervas daninhas', 'concluida'),

-- Família Lima
(5, 29, 32, 'Organizar festa', 'Preparar decoração e comidas', 'aprovada'),
(5, 30, 33, 'Lavar carros', 'Limpar os dois carros da família', 'pendente'),
(5, 31, 34, 'Arrumar computador', 'Fazer manutenção e backup', 'rejeitada'),
(5, 29, 35, 'Fazer feira', 'Comprar itens da lista', 'concluida'); 
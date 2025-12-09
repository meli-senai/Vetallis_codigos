USE vetallis_db_2_0;

# USUARIO #

INSERT INTO usuario (usuario_senha, usuario_email, usuario_nome, usuario_cpf, usuario_cargo) VALUES
('1234','teste@gmail.com','teste','12345678910','gerente');

 INSERT INTO usuario (usuario_senha, usuario_email, usuario_nome, usuario_cpf, usuario_cargo) VALUES
('5678','mariaeduardamartinscavallaro@gmail.com','Maria Eduarda Martins Cavallaro','49089469818','diretora'),
('9102','enzobueno@gmail.com','Enzo','49083719898','desempregado');

UPDATE usuario 
SET usuario_nome = 'Ana'
WHERE usuario_id = 1;

UPDATE usuario
SET usuario_cargo = 'professora'
WHERE usuario_id = 2;

UPDATE usuario
SET usuario_senha = '123a'
WHERE usuario_id = 3;

SELECT * 
FROM usuario;

SELECT usuario_nome 
FROM usuario
WHERE usuario_id = 3;

SELECT usuario_cargo, usuario_email
FROM usuario 
WHERE usuario_id = 2;

DELETE 
FROM usuario
WHERE usuario_id = 3;

DELETE 
FROM usuario
WHERE usuario_id = 1;

DELETE 
FROM usuario
WHERE usuario_id = 2;

# PRODUTO #

INSERT INTO produto (produto_nome, produto_quantidade, produto_descricao, produto_lote, produto_cod_barra, produto_categoria) VALUES
('dipirona',13,'cura dor de cabeca', '12A', '1234567890124', 'vacina'),
('novalgina',22,'tira cancer', '1514B', '23456789012374', 'comprimido'),
('B12',47,'bomba muscular', '27200C', '345679012345', 'xarope');

UPDATE produto
SET produto_nome = 'febre amarela'
WHERE produto_id = 1;

UPDATE produto
SET produto_quantidade = 2
WHERE produto_id = 2;

UPDATE produto
SET produto_lote = '145L'
WHERE produto_id = 3;

SELECT *
FROM produto;

SELECT produto_nome
FROM produto
WHERE produto_quantidade > 10;

SELECT produto_lote, produto_descricao
FROM produto
WHERE produto_id = 2;

DELETE 
FROM produto
WHERE produto_id = 1;

DELETE 
FROM produto
WHERE produto_id = 2;

DELETE 
FROM produto
WHERE produto_id = 3;

#PEDIDO SAIDA#

INSERT INTO pedido_saida (pedido_sida_lote, pedido_saida_nome, pedido_saida_categoria, pedido_saida_quantidade, usuario_usuario_id, produto_produto_id) VALUES
('1540M','paracetamol','comprimido', 2, 1, 4),
('2000P','losartana','xarope', 80, 2, 5),
('13999LU','rivotril','vacina', 200, 3, 6);

UPDATE pedido_saida
SET pedido_saida_nome = 'aspirina'
WHERE produto_produto_id = 4;

UPDATE pedido_saida
SET pedido_saida_categoria = 'vacina'
WHERE produto_produto_id = 5;

UPDATE pedido_saida
SET pedido_saida_quantidade = 38
WHERE produto_produto_id = 6;

SELECT *
FROM pedido_saida;

SELECT pedido_saida_nome
FROM pedido_saida
WHERE usuario_usuario_id = 2;

SELECT pedido_saida_nome, pedido_saida_quantidade
FROM pedido_saida
WHERE usuario_usuario_id = 3;

DELETE 
FROM pedido_saida
WHERE pedido_saida_id = 10;

DELETE 
FROM pedido_saida
WHERE pedido_saida_id = 11;

DELETE 
FROM pedido_saida
WHERE pedido_saida_id = 12;

#PEDIDO ENTRADA#

INSERT INTO pedido_entrada (pedido_ent_lote, pedido_ent_nome, pedido_ent_categoria, pedido_ent_quantidade,pedido_ent_descricao, usuario_usuario_id, produto_produto_id) VALUES
('1540M','paracetamol','comprimido', 2,'curar dor de cabeca', 1, 4),
('2000P','losartana','xarope', 80,'curar dor nas costas', 2, 5),
('13999LU','rivotril','vacina', 200,'passar vomito', 3, 6);

UPDATE pedido_entrada
SET pedido_ent_nome = 'aspirina'
WHERE produto_produto_id = 4;

UPDATE pedido_entrada
SET pedido_ent_categoria = 'vacina'
WHERE produto_produto_id = 5;

UPDATE pedido_entrada
SET pedido_ent_quantidade = 38
WHERE produto_produto_id = 6;

SELECT *
FROM pedido_entrada;

SELECT pedido_ent_nome
FROM pedido_entrada
WHERE usuario_usuario_id = 2;

SELECT pedido_ent_nome, pedido_ent_quantidade
FROM pedido_entrada
WHERE usuario_usuario_id = 3;

DELETE 
FROM pedido_entrada
WHERE pedido_ent_id = 4;

DELETE 
FROM pedido_entrada
WHERE pedido_ent_id = 5;

DELETE 
FROM pedido_entrada
WHERE pedido_ent_id = 6;

#LISTRA COMPRA#

INSERT INTO lista_compra (lista_compra_nome, lista_compra_quantidade, lista_compra_valor, lista_compra_status, produto_produto_id) VALUES
('comprar dipirona',12,50.00, 'vencendo',4),
('comprar losartana',100,200.00, 'esgotado',5),
('comprar novalgina',30,100.00, 'esgotando',6);

UPDATE lista_compra
SET lista_compra_nome = 'comprar aspirina'
WHERE produto_produto_id = 4;

UPDATE lista_compra
SET lista_compra_valor = 150.00
WHERE produto_produto_id = 5;

UPDATE lista_compra
SET lista_compra_status = 'venceu'
WHERE produto_produto_id = 6;

SELECT *
FROM lista_compra;

SELECT lista_compra_nome
FROM lista_compra
WHERE produto_produto_id = 5;

SELECT lista_compra_nome, lista_compra_valor
FROM lista_compra
WHERE produto_produto_id = 6;

DELETE 
FROM lista_compra
WHERE lista_compra_id = 1;

DELETE 
FROM lista_compra
WHERE lista_compra_id = 2;
DELETE 
FROM lista_compra
WHERE lista_compra_id = 3;

#CONTROLE SAIDA#

INSERT INTO  controle_saida(controle_saida_motivo, controle_saida_quantidade, controle_saida_nome, controle_saida_data, pedido_saida_pedido_saida_id) VALUES
('dor de barriga', 2, 'dipirona','2025-12-04', 13),
('verme', 3, 'vermifugo','2025-12-05', 14),
('colica', 5, 'buscopan','2025-12-06', 15);

UPDATE controle_saida
SET controle_saida_motivo = 'dor de cabeca'
WHERE pedido_saida_pedido_saida_id = 13;

UPDATE controle_saida
SET controle_saida_quantidade = 16
WHERE pedido_saida_pedido_saida_id = 14;

UPDATE controle_saida
SET controle_saida_data= '2025-12-03'
WHERE pedido_saida_pedido_saida_id = 15;

SELECT *
FROM controle_saida;

SELECT controle_saida_nome
FROM controle_saida
WHERE pedido_saida_pedido_saida_id = 14;

SELECT controle_saida_nome, controle_saida_data
FROM controle_saida
WHERE pedido_saida_pedido_saida_id = 15;

DELETE 
FROM controle_saida
WHERE controle_saida_id = 1;

DELETE 
FROM controle_saida
WHERE controle_saida_id = 2;

DELETE 
FROM controle_saida
WHERE controle_saida_id = 3;

#CONTROLE DE ENTRADA#

INSERT INTO  controle_entrada(controle_entrada_quantidade, controle_entrada_nome, controle_entrada_descricao, controle_entrada_data, pedido_entrada_pedido_ent_id) VALUES
(3,'dipirona', 'dor', '2025-12-04',7),
(4,'vermifugo', 'curar verme', '2025-12-05',8),
(5,'buscopan', 'colica', '2025-12-06',9);

UPDATE controle_entrada
SET controle_entrada_nome = 'buscofem'
WHERE pedido_entrada_pedido_ent_id = 13;

UPDATE controle_entrada
SET controle_entrada_quantidade = 16
WHERE pedido_entrada_pedido_ent_id = 14;

UPDATE controle_entrada
SET controle_entrada_data = '2025-12-03'
WHERE pedido_entrada_pedido_ent_id = 15;

SELECT *
FROM controle_entrada;

SELECT controle_entrada_nome
FROM controle_entrada
WHERE pedido_entrada_pedido_ent_id = 8;

SELECT controle_entrada_nome, controle_entrada_data
FROM controle_entrada
WHERE pedido_entrada_pedido_ent_id = 9;

DELETE 
FROM controle_entrada
WHERE controle_entrada_id = 1;

DELETE 
FROM controle_entrada
WHERE controle_entrada_id = 2;

DELETE 
FROM controle_entrada
WHERE controle_entrada_id = 3;

#HISTORICO SAIDA#

INSERT INTO historico_saida (historico_saida_quantidade, historico_saida_data, controle_saida_controle_saida_id)
VALUES (7, '2025-09-13', 4),
(9, '2025-09-01', 5),
(12, '2025-12-03', 6);

UPDATE historico_saida
SET historico_saida_quantidade = 16
WHERE controle_saida_controle_saida_id= 5;

UPDATE historico_saida
SET historico_saida_data = '2025-11-13'
WHERE controle_saida_controle_saida_id= 4;

UPDATE historico_saida
SET historico_saida_data = '2025-09-01'
WHERE controle_saida_controle_saida_id= 6;

SELECT * FROM historico_saida;

SELECT historico_saida_quantidade FROM historico_saida
WHERE  historico_saida_quantidade >10;

SELECT historico_saida_data FROM historico_saida
WHERE historico_saida_quantidade =12;

DELETE FROM historico_saida
WHERE controle_saida_controle_saida_id=4;

DELETE FROM historico_saida
WHERE controle_saida_controle_saida_id=5;

DELETE FROM historico_saida
WHERE controle_saida_controle_saida_id =6;

#HISTORICO ENTRADA#

INSERT INTO historico_entrada (historico_entrada_quantidade, historico_entrada_data, controle_entrada_controle_entrada_id) VALUES
( 20,'2025-12-04',4),
( 50,'2025-12-05',5),
(105, '2025-12-06', 6);

UPDATE historico_entrada
SET historico_entrada_data = '2026-01-05'
WHERE controle_entrada_controle_entrada_id =4;

UPDATE historico_entrada
SET historico_entrada_quantidade = 280 
WHERE controle_entrada_controle_entrada_id = 5;

UPDATE historico_entrada
SET historico_entrada_data= '2025-12-06'
WHERE controle_entrada_controle_entrada_id = 6; 

SELECT * FROM historico_entrada;

SELECT historico_entrada_data
FROM historico_entrada
WHERE controle_entrada_controle_entrada_id = 5;

SELECT historico_entrada_quantidade, historico_entrada_data
FROM historico_entrada
WHERE controle_entrada_controle_entrada_id= 6;

DELETE 
FROM historico_entrada
WHERE historico_entrada_id = 1;

DELETE 
FROM historico_entrada
WHERE historico_entrada_id = 2;

DELETE 
FROM historico_entrada
WHERE historico_entrada_id = 3;

#DADOS SENSOR#

INSERT INTO  dados_sensor(dados_sensor_nome, dados_sensor_tipo, dados_sensor_local, dados_sensor_status, dados_sensor_data_install) VALUES
('DHT11','umidade', 'cant parede sul', 'funcionando','2025-12-10'),
('RC522','rfid', 'cant parede norte', 'delay','2025-12-15'),
('lcd','display', 'cant parede oeste', 'quebrado','2025-12-20');

UPDATE dados_sensor
SET dados_sensor_nome = 'dht49'
WHERE dados_sensor_id = 1;

UPDATE dados_sensor
SET dados_sensor_tipo = 'calor'
WHERE dados_sensor_id = 2;

UPDATE dados_sensor
SET dados_sensor_local = 'parede norte'
WHERE dados_sensor_id = 3;

SELECT *
FROM dados_sensor;

SELECT dados_sensor_nome
FROM dados_sensor
WHERE dados_sensor_id = 2;

SELECT dados_sensor_nome, dados_sensor_tipo
FROM dados_sensor
WHERE dados_sensor_id = 3;

DELETE 
FROM dados_sensor
WHERE dados_sensor_id = 1;

DELETE 
FROM dados_sensor
WHERE dados_sensor_id = 2;

DELETE 
FROM dados_sensor
WHERE dados_sensor_id = 3;

#HISTORICO SENSOR#

insert into historico_sensor (historico_senso_rdados, dados_sensor_dados_sensor_id) values
("sensor parado",4),
("sensor quebrado",5),
("sensor funcionando",6);

update historico_sensor
set historico_senso_rdados = 'funcionando'
where dados_sensor_dados_sensor_id = 4;
update historico_sensor
set historico_senso_rdados = 'parado'
where dados_sensor_dados_sensor_id = 5;
update historico_sensor
set historico_senso_rdados = 'quebrado'
where dados_sensor_dados_sensor_id = 6;

select *
from historico_sensor;
select historico_senso_rdados
from historico_sensor
where dados_sensor_dados_sensor_id = 4;
select historico_senso_rdados
from historico_sensor
where dados_sensor_dados_sensor_id = 5;

delete 
from historico_sensor
where dados_sensor_dados_sensor_id = 4;
delete 
from historico_sensor
where dados_sensor_dados_sensor_id = 5;
delete 
from historico_sensor
where dados_sensor_dados_sensor_id = 6;








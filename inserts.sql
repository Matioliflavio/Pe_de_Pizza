CREATE TABLE  tb_pedido(
id_pedido       SERIAL NOT NULL,
id_cliente      INTEGER NOT NULL,
data_compra     DATE,
valor           NUMERIC(6,2),
CONSTRAINT pk_id_pedido PRIMARY KEY (id_pedido),
CONSTRAINT fk_tb_cliente_id_cliente FOREIGN KEY (id_cliente) REFERENCES tb_clientes(id_cliente)
);

CREATE TABLE tb_item_pedido(
id_item         SERIAL NOT NULL,
id_pedido       INTEGER NOT NULL, 
id_pizza        INTEGER NOT NULL,
quantidade      INTEGER, 
fg_meia         INTEGER,
valor           NUMERIC(5,2),
CONSTRAINT pk_item_pedido PRIMARY KEY (id_pedido, id_pizza, id_item),
CONSTRAINT fk_tb_pedido_id_pedido FOREIGN KEY (id_pedido) REFERENCES tb_pedido(id_pedido),
CONSTRAINT fk_tb_pizzas_id_pizza FOREIGN KEY (id_pizza) REFERENCES tb_pizzas(id_pizza)            
);

insert INTO tb_pedido(id_cliente, data_compra, valor) VALUES (1, '2018-04-02', 50.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (1, 1, 1, 1, 0, 25.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (2, 1, 2, 1, 0, 25.00);

insert INTO tb_pedido(id_cliente, data_compra, valor) VALUES (2, '2018-04-02', 75.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (3, 2, 1, 1, 0, 25.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (4, 2, 2, 1, 0, 25.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (5, 2, 3, 1, 0, 25.00);

insert INTO tb_pedido(id_cliente, data_compra, valor) VALUES (3, '2018-04-02', 95.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (6, 3, 4, 1, 0, 30.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (7, 3, 5, 1, 0, 30.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (8, 3, 6, 1, 0, 35.00);


insert INTO tb_pedido(id_cliente, data_compra, valor) VALUES (4, '2018-04-03', 88.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (9, 4, 7, 1, 0, 44.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (10, 4, 8, 1, 1, 22.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (11, 4, 9, 1, 1, 22.00);


insert INTO tb_pedido(id_cliente, data_compra, valor) VALUES (5, '2018-04-03', 95.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (12, 5, 9, 1, 1, 22.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (13, 5, 10, 1, 1, 22.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (14, 5, 1, 1, 1, 22.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (15, 5, 11, 1, 1, 22.00);

insert INTO tb_pedido(id_cliente, data_compra, valor) VALUES (6, '2018-04-03', 185.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (16, 6, 2, 2, 0, 30.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (17, 6, 3, 2, 0, 30.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (18, 6, 4, 2, 0, 35.00);

insert INTO tb_pedido(id_cliente, data_compra, valor) VALUES (7, '2018-04-04', 132.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (19, 7, 7, 1, 0, 44.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (20, 7, 8, 2, 0, 22.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (21, 7, 9, 2, 0, 22.00);

insert INTO tb_pedido(id_cliente, data_compra, valor) VALUES (8, '2018-05-01', 132.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (22, 8, 10, 1, 0, 44.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (23, 8, 4, 2, 0, 22.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (24, 8, 9, 2, 0, 22.00);

insert INTO tb_pedido(id_cliente, data_compra, valor) VALUES (9, '2019-05-02', 132.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (25, 9, 5, 1, 0, 44.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (26, 9, 3, 2, 0, 22.00);
insert INTO tb_item_pedido(id_item, id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES (27, 9, 1, 2, 0, 22.00);

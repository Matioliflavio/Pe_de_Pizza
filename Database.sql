--Tabelas do projeto
CREATE DATABASE bd_pedepizza;

DROP TABLE tb_item_pedido;
DROP TABLE tb_pedido;
DROP TABLE tb_pizzas;
DROP TABLE tb_clientes;

CREATE TABLE tb_clientes(
id_cliente      SERIAL NOT NULL, 
nome            VARCHAR(30) NOT NULL,
telefone        VARCHAR(14) NOT NULL,
cep             VARCHAR(9),
rua             VARCHAR(40),
numero          VARCHAR(6),
complemento     VARCHAR(10),
bairro          VARCHAR(20),
CONSTRAINT pk_id_cliente PRIMARY KEY (id_cliente)
);

CREATE TABLE tb_pizzas(
id_pizza    SERIAL NOT NULL,
sabor       VARCHAR(20),
valor       NUMERIC(5,2),
CONSTRAINT pk_id_pizza PRIMARY KEY (id_pizza)
);

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

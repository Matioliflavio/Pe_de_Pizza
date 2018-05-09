--Tabelas do projeto


CREATE TABLE clientes(
id_cliente      SERIAL NOT NULL, 
nome            VARCHAR(30) NOT NULL,
telefone        VARCHAR(13) NOT NULL,
rua             VARCHAR(40),
numero          VARCHAR(6),
complemento     VARCHAR(10),
bairro          VARCHAR(20)
CONSTRAINT pk_id_cliente PRIMARY KEY (id_cliente)
);

CREATE TABLE pizzas(
id_pizza    SERIAL NOT NULL,
sabor       VARCHAR(20),
valor       NUMERIC(5,2),
CONSTRAINT pk_id_pizza PRIMARY KEY (id_pizza)
);

CREATE TABLE  pedido(
id_pedido       SERIAL NOT NULL PRIMARY KEY,
id_cliente      INTEGER NOT NULL,
data_compra     DATE,
valor           NUMERIC(6,2),
CONSTRAINT pk_id_pedido PRIMARY KEY (id_pedido),
CONSTRAINT fk_tb_cliente_id_cliente FOREIGN KEY (id_clientte) REFERENCES clientes(id_cliente)
);

CREATE TABLE item_pedido(
id_pedido       INTEGER NOT NULL, 
id_pizza        INTEGER NOT NULL,
quantidade      INTEGER, 
fg_meia         INTEGER,
CONSTRAINT pk_item_pedido PRIMARY KEY (id_pedido, id_pizza),
CONSTRAINT fk_tb_pedido_id_pedido FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido),
CONSTRAINT fk_tb_pizzas_id_pizza FOREIGN KEY (id_pizza) REFERENCES pizzas(id_pizza)            
);

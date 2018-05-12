##Classe de manipulação de dados
# para instalar o driver -> pip install psycopg2

import psycopg2 as pg
import datetime as dt

log = True #Habilita log

def log(data):
    if log: print(data)

def conecta():
    con = pg.connect(database="bd_pedepizza", user="postgres", password="qwerty", host="127.0.0.1", port="5432")
    log("sucesso na conexão")
    return con

def desconecta(con):
    con.commit()
    con.close()
    log("conexão encerrada")

#////////////////////////////////
#//////////  INSERTS  ///////////
#////////////////////////////////

def insere_cliente(nome, telefone, rua=None, numero=None, complemento=None, bairro= None):
    sql = "INSERT INTO tb_clientes(nome, telefone, rua, numero, complemento, bairro ) VALUES(%s, %s, %s, %s, %s, %s) RETURNING id_cliente;"
    id_cliente = None
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(cur.mogrify(sql, (nome, telefone, rua, numero, complemento, bairro)))
        id_cliente = cur.fetchone()[0]
        log("Cliente id: " + str(id_cliente) + " inserido com sucesso!")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
        return 0 
    return id_cliente

def insere_pizza(sabor, valor):
    sql = "INSERT INTO tb_pizzas(sabor, valor) VALUES(%s, %s) RETURNING id_pizza;"
    id_pizza = None
    log("Inserindo Pizza " + sabor)
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(cur.mogrify(sql, (sabor, valor)))
        id_pizza = cur.fetchone()[0]
        log("Pizza id: " + str(id_pizza) + " inserida com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
        return 0
    return id_pizza

def insere_pedido(id_cliente):
    sql = "INSERT INTO tb_pedido(id_cliente, data_compra) VALUES(%s, %s) RETURNING id_pedido;"
    id_pedido = None
    data = dt.date.today().strftime("%d/%m/%Y")
    log("Inserindo pedido")
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(cur.mogrify(sql, (id_cliente, data)))
        id_pedido = cur.fetchone()[0]
        log("Pedido id: " + str(id_pedido) + " inserido com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
        return 0
    return id_pedido

def insere_item_pedido(id_pedido, id_pizza, quantidade, fg_meia, valor):#dados devem ser tratados antes de vir.
    sql = "INSERT INTO tb_item_pedido(id_pedido, id_pizza, quantidade, fg_meia, valor) VALUES(%s, %s, %s, %s, %s);"
    log("Inserindo item pedido")
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(cur.mogrify(sql, (id_pedido, id_pizza, quantidade, fg_meia, valor)))
        log("Item inserido com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
        return 0
    return 1

def finaliza_pedido(id_pedido, valor):
    sql = "UPDATE tb_pedido SET valor = %s WHERE id_pedido = %s;"
    log("Atualizando pedido")
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(cur.mogrify(sql, (valor, id_pedido)))
        log("Pedido atualizado com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
        return 0
    return 1


log("insere dados")
#--TESTES DE INSERSÃO----
#insere_cliente("Veronica Matioli", "(16)98888-4321", "dos pinhais", 31, None, "alcantara" )
#insere_pizza("Quatro Queijos", 32.90)
#insere_pedido(3)
#insere_item_pedido(1, 1, 2, 0, 65.80)
#finaliza_pedido(2, 44.50)
log("final insere dados")


#////////////////////////////////
#//////////  SELECTS  ///////////
#////////////////////////////////


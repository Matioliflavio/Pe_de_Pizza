##Classe de manipulação de dados
# para instalar o driver -> pip install psycopg2

import psycopg2 as pg
import datetime as dt

log = True #Habilita log

def log(data):
    if log: print(data)

def conecta():
    con = pg.connect(database="bd_pedepizza", user="postgres", password="qwerty", host="127.0.0.1", port="5432")
    log("Sucesso na conexão")
    return con

def desconecta(con):
    con.commit()
    con.close()
    log("Conexão encerrada")


#////////////////////////////////
#//////////  INSERTS  ///////////
#////////////////////////////////


def insere_cliente(nome, telefone, cep=None, rua=None, numero=None, complemento=None, bairro= None, flag=1):
    sql = "INSERT INTO tb_clientes(nome, telefone, cep, rua, numero, complemento, bairro, fg_ativo ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id_cliente;"
    id_cliente = None
    fgAtivo = 1
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(cur.mogrify(sql, (nome, telefone, cep, rua, numero, complemento, bairro, fgAtivo)))
        id_cliente = cur.fetchone()[0]
        log("Cliente id: " + str(id_cliente) + " inserido com sucesso!")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
        return 0 
    return id_cliente

def insere_pizza(sabor, valor, flag):
    sql = "INSERT INTO tb_pizzas(sabor, valor, fg_ativo) VALUES(%s, %s, %s) RETURNING id_pizza;"
    id_pizza = None
    fgAtivo = 1
    log("Inserindo Pizza " + sabor)
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(cur.mogrify(sql, (sabor, valor, fgAtivo)))
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


#////////////////////////////////
#//////////  SELECTS  ///////////
#////////////////////////////////


def lista_clientes():
    sql = "SELECT * FROM tb_clientes WHERE fg_ativo = 1;"
    log("Buscando Todos os clientes")
    clientes = None
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(sql)
        clientes = cur.fetchall()
        log("Itens retornados com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
    return clientes #mesmo com erro retorna None
    
def lista_pizzas():
    sql = "SELECT * FROM tb_pizzas WHERE fg_ativo = 1;"
    log("Buscando todas os pizzas")
    pizzas = None
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(sql)
        pizzas = cur.fetchall()
        log("Itens retornados com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
    return pizzas #mesmo com erro retorna None

def lista_cliente_por_id(id):
    sql = "SELECT * FROM tb_clientes WHERE id_cliente = %s AND fg_ativo = 1;"
    log("Buscando cliente id: " %str(id))
    cliente = None
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(cur.mogrify(sql, (str(id))))
        cliente = cur.fetchone()
        log("Item retornado com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
    return cliente #mesmo com erro retorna None

def lista_pizza_por_id(id):
    sql = "SELECT * FROM tb_pizzas WHERE id_pizza = %s AND fg_ativo = 1;"
    log("Buscando pizza id: %s" %str(id)) 
    pizza = None
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(cur.mogrify(sql, (str(id))))
        pizza = cur.fetchone()
        log("Item retornado com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
    return pizza #mesmo com erro retorna None

def busca_clientes(parcial):
    sql = "SELECT * FROM tb_clientes WHERE nome LIKE %(like)s AND fg_ativo = 1;"
    log("Buscando Todos os clientes")
    clientes = None
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(sql, dict(like= '%'+parcial.upper()+'%'))
        clientes = cur.fetchall()
        log("Itens retornados com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
    return clientes #mesmo com erro retorna None

def faturamento_do_dia(data):
    sql = "SELECT SUM(valor) FROM tb_pedido WHERE data_compra = %s;"
    #data = dt.date.today().strftime("%Y-%m-%d")
    log("Somando Faturamento: %s" %data)
    fatura = None
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(cur.mogrify(sql, (data,) ))
        fatura = cur.fetchone()
        log("Item retornado com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
    return fatura #mesmo com erro retorna None

def faturamento_do_mes(mes, ano):
    sql = "SELECT SUM(p.valor) FROM tb_pedido p WHERE (EXTRACT(YEAR FROM p.data_compra) = %s AND EXTRACT(MONTH FROM p.data_compra) =  %s);"
    log("Somando Faturamento do mês: %s" %mes)
    fatura = None
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(cur.mogrify(sql, (ano, mes,) ))
        fatura = cur.fetchone()
        log("Item retornado com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
    return fatura #mesmo com erro retorna None

def faturamento_do_ano(ano):
    sql = "SELECT SUM(valor) FROM tb_pedido WHERE EXTRACT(YEAR FROM data_compra) = %s;"
    log("Somando Faturamento do ano: %s" %ano)
    fatura = None
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(cur.mogrify(sql, (ano,) ))
        fatura = cur.fetchone()
        log("Item retornado com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
    return fatura #mesmo com erro retorna None

def maisVendida():
    sql = "SELECT SUM(i.quantidade),p.sabor FROM tb_pizzas p, tb_item_pedido i WHERE i.id_pizza = p.id_pizza GROUP BY p.id_pizza ORDER BY SUM(i.quantidade) DESC;"
    log("Buscando pizzas favoritas ")
    dados = None
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(sql)
        dados = cur.fetchmany(5)
        log("Pesquisa efetuada com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
    return dados #mesmo com erro retorna None

def melhoresClientes():
    sql = "SELECT c.nome, SUM(p.valor) FROM tb_pedido p, tb_clientes c WHERE p.id_cliente = c.id_cliente GROUP BY c.id_cliente ORDER BY SUM(p.valor) DESC;"
    log("Buscando melhores clientes ")
    cliente = None
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(sql)
        cliente = cur.fetchmany(5)
        log("Pesquisa efetuada com sucesso")
        desconecta(con)
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
    return cliente #mesmo com erro retorna None


    #//////////////////////////////////
    #//////////  "DELETES"  ///////////
    #//////////////////////////////////

def deleta_cliente_por_id(id):
    sql = "UPDATE tb_clientes SET fg_ativo = 0 WHERE id_cliente = %(like)s;"
    log("Buscando cliente id: %s" %str(id))
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(sql, dict(like= id))
        log("Item deletado com sucesso")
        desconecta(con)
        return 1
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
        return 0

def deleta_pizza_por_id(id):
    sql = "UPDATE tb_pizzas SET fg_ativo = 0 WHERE id_pizza = %(like)s;"
    log("Buscando pizza id: %s" %str(id))
    try:
        con = conecta()
        cur = con.cursor()
        cur.execute(sql, dict(like= id))
        log("Item deletado com sucesso")
        desconecta(con)
        return 1
    except (Exception, pg.DatabaseError) as erro:
        log(erro)
        return 0 
<<<<<<< HEAD
=======

a = melhoresClientes()
print(a)

>>>>>>> af5f145f0a34bfed6e9ad9d07c322ed62a8bf32c

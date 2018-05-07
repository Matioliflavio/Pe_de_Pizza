##Classe de manipulação de dados
# para instalar o driver -> pip install psycopg2
#Será que isso funciona?!

import psycopg2


#insere cliente e retorna com o id
def insere_cliente(nome, telefone, rua=None, numero=None, complemento=None, bairro= None):
    sql = "INSERT INTO clientes(nome, ) VALUES(%s, %s, %s, %s, %s, %s) RETURNING id_cliente;"##precisa ajustar isso
    conn = None
    id_cliente = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (nome, telefone, rua, numero, complemento, bairro))
        # get the generated id back
        id_cliente = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return vendor_id_cliente
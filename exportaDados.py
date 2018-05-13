import json
import ManipuladorDados as mp


log = True #Habilita log

def log(data):
    if log: print(data)

def cria_backup_json():
    log("Iniciando Backup!")
    data = {} #objeto que será o JSON
    pizzas = []
    log("Adicionado Pizzas")
    pizzas_do_banco = mp.lista_pizzas()
    for item in pizzas_do_banco:
        pizza = {}
        pizza["id_pizza"] = item[0]
        pizza["sabor"] = item[1]
        pizza["valor"] = float(item[2])
        pizzas.append(pizza)

    data["pizzas"] = pizzas

    clientes = []
    log("Adicionando Clientes")
    clientes_do_banco = mp.lista_clientes()
    for item in clientes_do_banco:
        cliente = {}
        cliente["id_cliente"] = item[0]
        cliente["nome"] = item[1]
        cliente["telefone"] = (item[2])
        cliente["rua"] = item[3]
        cliente["numero"] = item[4]
        cliente["complemento"] = item[5]
        cliente["bairro"] = item[6]
        clientes.append(cliente) 

    data["clientes"] = clientes

    log("Criando arquivo JSON")
    f = open("backup.json", "w") #cria o arquivo
    json.dump(data, f, sort_keys=True, indent=4) #junta tudo no JSON
    f.close()

#aqui entra a zica da compactação! :P
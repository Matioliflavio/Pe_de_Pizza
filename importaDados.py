#Arquvivo 100% funcional
#função recebe uma url e insere todos os dados no banco. 
#Não ha verificação de dados quanto ao arquivo importado 

import json
import requests
import ManipuladorDados as mp

#Arquivo JSON: https://docs.google.com/uc?export=download&id=1kFWv_Dfq9hCJrz3b2BTMjx1Z2JxifBDg

log = True #Habilita log console
verbose = True

def log(data):
    if log : print(data)


url = "https://docs.google.com/uc?export=download&id=1kFWv_Dfq9hCJrz3b2BTMjx1Z2JxifBDg" 

def importa_dados(url):
    result = []
    urldata = requests.get(url)
    jsondata = urldata.json()
    result.append("CLIENTES:")
    for cliente in jsondata["clientes"]:
        log("Inserindo cliente id: " + str(cliente["id_cliente"]))
        mp.insere_cliente(cliente["nome"],
        cliente["telefone"],
        cliente["cep"],
        cliente["rua"],
        cliente["numero"],
        cliente["complemento"],
        cliente["bairro"],
        cliente["fg_ativo"])
        result.append(cliente)

    log("Clientes inseridos com sucesso!")
    result.append("PIZZAS: ")
    for pizza in jsondata["pizzas"]:
        log("Inserindo pizza id: " + str(pizza["id_pizza"]))
        mp.insere_pizza(pizza["sabor"], pizza["valor"], pizza["fg_ativo"])
        result.append(pizza)

    log("Pizzas inseridas com sucesso!")
    return result
#print(importa_dados(url)) # descomente para funcionar
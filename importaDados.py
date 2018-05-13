#Arquvivo 100% funcional
#função recebe uma url e insere todos os dados no banco. 
#Não ha verificação de dados quanto ao arquivo importado 

import json
import requests
import ManipuladorDados as mp

#Arquivo JSON: https://docs.google.com/uc?export=download&id=1kFWv_Dfq9hCJrz3b2BTMjx1Z2JxifBDg

log = True

def log(data):
    if log : print(data)

url = "https://docs.google.com/uc?export=download&id=1kFWv_Dfq9hCJrz3b2BTMjx1Z2JxifBDg" 

def importa_dados(url):
    urldata = requests.get(url)
    jsondata = urldata.json()
    for cliente in jsondata["clientes"]:
        log("Inserindo cliente id: " + str(cliente["id_cliente"]))
        mp.insere_cliente(cliente["nome"],
        cliente["telefone"],
        cliente["rua"],
        cliente["numero"],
        cliente["complemento"],
        cliente["bairro"])

    log("Clientes inseridos com sucesso!")

    for pizza in jsondata["pizzas"]:
        log("Inserindo pizza id: " + str(pizza["id_pizza"]))
        mp.insere_pizza(pizza["sabor"], pizza["valor"])

    log("Pizzas inseridas com sucesso!")

importa_dados(url) # descomente para funcionar
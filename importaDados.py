import json
import requests
import ManipuladorDados as mp

#Arquivo JSON: https://docs.google.com/uc?export=download&id=1kFWv_Dfq9hCJrz3b2BTMjx1Z2JxifBDg

log = True

def log(data):
    if log : print(data)

#url = input("digite a URL: ") #INPUT
url = "https://docs.google.com/uc?export=download&id=1kFWv_Dfq9hCJrz3b2BTMjx1Z2JxifBDg" #descomente para OVERRIDE



def importa_dados(url):
    urldata = requests.get(url)
    jsondata = urldata.json()
    for cliente in jsondata["clientes"]:
        log("Inserindo id: " + str(cliente["id_cliente"]))
        mp.insere_cliente(cliente["nome"],
        cliente["telefone"],
        cliente["rua"],
        cliente["numero"],
        cliente["complemento"],
        cliente["bairro"])

    log("Clientes inseriidos com sucesso")

    for pizza in jsondata["pizzas"]:
        log("inserindo Pizza id: " + str(pizza["id_pizza"]))
        mp.insere_pizza(pizza["sabor"], pizza["valor"])

    log("pizzas inseridas com sucesso")

importa_dados(url)
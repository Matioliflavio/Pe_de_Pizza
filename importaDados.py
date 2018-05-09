import json
import requests

#Arquivo JSON: https://docs.google.com/uc?export=download&id=1kFWv_Dfq9hCJrz3b2BTMjx1Z2JxifBDg

url = input("digite a URL: ") #INPUT
url = "https://docs.google.com/uc?export=download&id=1kFWv_Dfq9hCJrz3b2BTMjx1Z2JxifBDg" #OVERRIDE

urldata = requests.get(url)
jsondata = urldata.json()
for cliente in jsondata["clientes"]:
    print("id: %d \tnome: %s" %(cliente["id"], cliente["nome"].capitalize()))



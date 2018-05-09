import json

data = {} #objeto que será o JSON

pizza = {} #dicionario para uma pizza
pizza["id"] = 1
pizza["sabor"] = "MINEIRA"
pizza["valor"] = 25.30

data["pizzas"] = pizza

cliente = {} #dicionario para um cliente
cliente["id"] = 1
cliente["nome"] = "PAULO PAULADA"
cliente["telefone"] = "(16)99999-1111"
cliente["rua"] = "DAS OLIVEIRAS"
cliente["numero"] = "69"
cliente["complemento"] = "AP 104"
cliente["bairro"] = None

clientes=[] #lista para varios clientes
clientes.append(cliente)

cliente["id"] = 2
cliente["nome"] = "PAULO PAULADA POWER"
cliente["telefone"] = "(16)99999-2222"
cliente["rua"] = "DAS PARREIRAS"
cliente["numero"] = "96"
cliente["complemento"] = "AP 200"
cliente["bairro"] = None

clientes.append(cliente)
data["clientes"] = clientes


f = open("teste.json", "w") #cria o arquivo
json.dump(data, f, sort_keys=True, indent=4) #junta tudo no JSON
f.close()

#aqui entra a zica da compactação! :P
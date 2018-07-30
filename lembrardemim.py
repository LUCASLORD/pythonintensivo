import json

username = input("Qual seu nome: ")
filename = 'usuario.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("Nós iremos nos lembrar quando você voltar {} !".format(username))

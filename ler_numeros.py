import json

filename = 'numeros.json'

with open(filename) as f_obj:
    numeros = json.load(f_obj)
    print(numeros)

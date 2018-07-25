pessoa = {
            'nome': 'Lucas',
            'sobrenome': 'Silva',
            'idade': 30,
            'cidade': 'Marília'}

print(pessoa)

for chave, valor in pessoa.items():
    print("\nChave: {}".format(chave))
    print("Valor: {}".format(valor))

if 'carro' not in pessoa.keys():
    print('carro')

if 'carro' not in pessoa.items():
    print('carro2')

for chave in sorted(pessoa.keys()):
    print(chave)

for valor in sorted(pessoa.items()):
    print(valor)

for valor in pessoa.values():
    print(valor)


rios = {    
            'nilo': 'egito',
            'amazonas': 'brasil',
            'prata': 'argentina'}

for chave, valor in rios.items():
    print("O {} corre por {}".format(chave, valor))

for chave in rios.keys():
    print(chave)

for valor in rios.values():
    print(valor)

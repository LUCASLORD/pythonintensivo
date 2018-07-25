linguagem_favorita = {'jen': ['python', 'ruby'], 'sarah': ['c'], 'edward': ['ruby','go']}

for nome, linguagens in linguagem_favorita.items():
    print("\n{} linguagem favorita:".format(nome.title()))
    for linguagem in linguagens:
        print("\t{}".format(linguagem.title()))

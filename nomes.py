from funcao_nome import get_nome_formatado

print("Aperte 'q' para sair")

while True:

    primeiro = input("\n Informe o primeiro nome: ")
    if primeiro == 'q':
        break

    segundo = input("\n Informe o segundo nome: ")
    if segundo == 'q':
        break

    nome_formatado = get_nome_formatado(primeiro, segundo)

    print("\t Nome Formatado {}.".format(nome_formatado))

# print(5/0) dará um erro ZeroDivisionError iremos tratar

try:
    print("tentar dividir 5 por 0")
    print(5/0)
except ZeroDivisionError:
    print("Você não pode dividir por 0!")

print("===========================================================")
print("Calculadora de divisão\n")

print("Me de 2 números e irei dividir")
print("Aperte 'q' para sair")

while True:
    primeiro_numero = input("\n Primeiro Número: ")
    if primeiro_numero == 'q':
        break
    segundo_numero = input("\n Segundo Número: ")
    if segundo_numero == 'q':
        break
    
    try:
        resposta = int(primeiro_numero) / int(segundo_numero)
    except ZeroDivisionError:
        print("Você não pode dividir por 0!")
    else:
        print(resposta)

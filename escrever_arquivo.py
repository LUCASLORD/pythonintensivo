filename = 'programando.txt'

with open(filename, 'w') as file_object:
    file_object.write("Amo Programar.\n")
    file_object.write("Gosto de Jogos.\n")

#concatenar em arquivo já existente

with open(filename, 'a') as file_object:
    file_object.write("Gosto de procurar coisas.\n")
    file_object.write("Gosto de aplicativos.\n")

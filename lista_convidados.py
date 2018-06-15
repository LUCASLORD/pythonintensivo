convidados = ["Lucas", "Gustavo", "Carla"]

print("{} Você está convidado(a) para meu jantar".format(convidados[0]))
print("{} Você está convidado(a) para meu jantar".format(convidados[1]))
print("{} Você está convidado(a) para meu jantar".format(convidados[2]))

print("{} não poderá comparacer".format(convidados[1]))

convidados[1] = "Marcos"

print("{} Você está convidado(a) para meu jantar".format(convidados[0]))
print("{} Você está convidado(a) para meu jantar".format(convidados[1]))
print("{} Você está convidado(a) para meu jantar".format(convidados[2]))

print("Encontrei Angra, Kamelot e Shaman numa mesa maior")


print(convidados)

convidados.insert(0,"Angra")
convidados.insert(2,"Kamelot")
convidados.append("Shaman")

print("{} Você está convidado(a) para meu jantar".format(convidados[0]))
print("{} Você está convidado(a) para meu jantar".format(convidados[1]))
print("{} Você está convidado(a) para meu jantar".format(convidados[2]))
print("{} Você está convidado(a) para meu jantar".format(convidados[3]))
print("{} Você está convidado(a) para meu jantar".format(convidados[4]))
print("{} Você está convidado(a) para meu jantar".format(convidados[5]))

print("Agora só posso convidar duas pessoas")

removido = convidados.pop(3)
print("{} Você foi Desconvidado".format(removido))

print("{} Você está convidado(a) para meu jantar".format(convidados[0]))
print("{} Você está convidado(a) para meu jantar".format(convidados[1]))
print("{} Você está convidado(a) para meu jantar".format(convidados[2]))
print("{} Você está convidado(a) para meu jantar".format(convidados[3]))
print("{} Você está convidado(a) para meu jantar".format(convidados[4]))

removido = convidados.pop(2)
print("{} Você foi Desconvidado".format(removido))

print("{} Você está convidado(a) para meu jantar".format(convidados[0]))
print("{} Você está convidado(a) para meu jantar".format(convidados[1]))
print("{} Você está convidado(a) para meu jantar".format(convidados[2]))
print("{} Você está convidado(a) para meu jantar".format(convidados[3]))

removido = convidados.pop(2)
print("{} Você foi Desconvidado".format(removido))

print("{} Você está convidado(a) para meu jantar".format(convidados[0]))
print("{} Você está convidado(a) para meu jantar".format(convidados[1]))
print("{} Você está convidado(a) para meu jantar".format(convidados[2]))

removido = convidados.pop(0)
print("{} Você foi Desconvidado".format(removido))

print("{} Você está convidado(a) para meu jantar".format(convidados[0]))
print("{} Você está convidado(a) para meu jantar".format(convidados[1]))

del convidados[0]
del convidados[0]

print(convidados)
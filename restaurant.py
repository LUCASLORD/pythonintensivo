class Restaurante():

    def __init__(self, nome_restaurante, tipo_cozinha):
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha

    def descricao(self):
        print("Restaurante {}, especialista em comida {}".format(self.nome_restaurante, self.tipo_cozinha))
    
    def abrir_restaurante(self):
        print("Restaurante {} está aberto".format(self.nome_restaurante))

class Usuario():

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def descricao(self):
        print(self.nome)
        print(self.sobrenome)
    
    def cumprimento(self):
        print("Ola {} {}".format(self.nome, self.sobrenome))



restaurante = Restaurante("Tropeiro", "Caseira")

print(restaurante.nome_restaurante)
print(restaurante.tipo_cozinha)

restaurante.descricao()
restaurante.abrir_restaurante()

usuario = Usuario("Lucas", "Silva")
print(usuario.nome)
print(usuario.sobrenome)
usuario.descricao()
usuario.cumprimento()



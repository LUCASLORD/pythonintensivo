class Dog():
    '''Uma tentativa simples de modelar um cachorro'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sentar(self):
        '''Simula um cachorro sentando em resposta um comando'''
        print("{} está sentando".format(self.name))

    def roll_over(self):
        '''Simula um cachorro rolando em resposta a um comando'''
        print("{} está rolando".format(self.name))



meu_cachorro = Dog('rex', 6)

print(meu_cachorro.name)
print(meu_cachorro.age)

meu_cachorro.sentar()
meu_cachorro.rolar()

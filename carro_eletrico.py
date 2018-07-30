class Carro():

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.leitura_odometro = 0
        self.tanque = 0

    def get_nome_descritivo(self):
        longo_nome = str(self.ano) + ' ' + self.marca + ' ' + self.modelo
        return longo_nome.title()

    def ler_odometro(self):
        print("Carro tem: {} milhas".format(self.leitura_odometro))

    def update_odometro(self, milhagem):
        if milhagem >= self.leitura_odometro:
            self.leitura_odometro = milhas
        else:
            print("Você não pode voltar o odometro")

    def incrementa_odometro(self, milhas):
        self.leitura_odometro += milhas
    
    def encher_tanque(self, litros):
        self.tanque += litros
        print("Você colocou {} litros no tanque".format(litros))

class CarroEletrico(Carro):
    '''Representa aspectos de veiculos Eletricos'''
    
    def __init__(self, marca, modelo, ano):
        '''inicializa os atributos da classe-pai'''
        super().__init__(marca, modelo, ano)
        self.tamanho_bateria = 70

    def descreve_bateria(self):
        '''Exibe a descrição da bateria'''
        print("O carro tem uma bateria de {} -kwh".format(self.tamanho_bateria))

    def encher_tanque(self):
        print("Carros Elétricos não tem tanque de gasolina")



meu_tesla = CarroEletrico('tesla', 'model s', '2018')

print(meu_tesla.get_nome_descritivo())
meu_tesla.descreve_bateria()
meu_tesla.encher_tanque()

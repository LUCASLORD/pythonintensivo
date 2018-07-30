class PesquisaAnonima():
    """Coleta respostas anonimas para uma pergunta de uma pesquisa"""

    def __init__(self, question):
        """Armazena uma pergunta e se prepara para armazenar as respostas."""
        self.question = question
        self.respostas = []

    def mostrar_pergunta(self):
        """Mostra a pergunta da pesquisa"""
        print(self.question)

    def salva_resposta(self, nova_resposta):
        """Armazena uma única resposta da pesquisa."""
        self.respostas.append(nova_resposta)

    def mostra_resultado(self):
        """Mostra todas as respostas dadas."""
        print("Resultados da Pesquisa: ")
        for resposta in self.respostas:
            print("- {}".format(resposta))

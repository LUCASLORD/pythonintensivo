from pesquisa import PesquisaAnonima

#Define uma pergunta e cria uma pesquisa 
questao = "Qual língua você aprendeu a falar primeiro"
minha_pesquisa = PesquisaAnonima(questao)

#Mostra a pergunta e armazena as respostas à pergunta
minha_pesquisa.mostrar_pergunta()
print("Aperte 'q' para sair.\n")

while True:
    resposta = input("Língua: ")
    
    if resposta == 'q':
        break
    
    minha_pesquisa.salva_resposta(resposta)
    
#Exive os resultados da pesquisa
print("\n Obrigado por participar da pesquisa")
minha_pesquisa.mostra_resultado()

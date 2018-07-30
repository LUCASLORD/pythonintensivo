def greet_user(username):
    '''Exibe uma saudação simples.'''
    print("Hello {} !".format(username.title()))

greet_user("Lucas")


def display_message():
    print("Funções")

display_message()

def favorite_book(title):
    print("Livro favorito {}".format(title.title()))

favorite_book("Python Intensivo")

def make_shirt(tamanho_texto, menssagem="Python"):
    print("tamanho do texto:{}, mensagem:  {}".format(tamanho_texto,menssagem))

make_shirt(10)

def make_pizza(*args):
    '''Exibe a lista de ingredientes pedidos.'''
    print("recebe uma lista como parametro")
    print(args)

make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **kwargs):
    '''Constrói um dicionário contendo tudo que sabemos sobre usuário'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in kwargs.items():
        profile[key] = value
    
    return profile

user_profile = build_profile('Lucas', 'Silva', location='marilia', field='Engineering')
print(user_profile)

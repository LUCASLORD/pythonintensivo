def get_nome_formatado(primeiro, segundo, ultimo=''):
    '''Gera um nome completo formatdado de modo elegante'''

    nome_completo = primeiro + ' ' + segundo + ' ' + ultimo
    return nome_completo.title().strip()

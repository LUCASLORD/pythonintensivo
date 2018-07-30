import unittest

from funcao_nome import get_nome_formatado


class NomeTestCase(unittest.TestCase):
    """Testes para 'name_funcition.py'."""

    def test_primeiro_segundo_nome(self):
        """Nomes Como 'Lucas Gustavo' funcionam?"""

        nome_formatado = get_nome_formatado('lucas', 'gustavo')
        self.assertEqual(nome_formatado, 'Lucas Gustavo')

    def test_primeiro_segundo_ultimo_nome(self):
        """Nomes como 'Wolfgang Amadeus Mozart' funcionam?"""

        nome_formatado = get_nome_formatado('wolfgang', 'Amadeus', 'mOZART')
        self.assertEqual(nome_formatado, 'Wolfgang Amadeus Mozart')


unittest.main()

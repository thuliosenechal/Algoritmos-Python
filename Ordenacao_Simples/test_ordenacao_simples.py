import unittest

from ordenacao_simples import ordenacao_simples


class TestOrdenacaoSimples(unittest.TestCase):

    def test_case_a(self):
        lista = [4, 8, 2, 1, 6, 10]
        self.assertEqual(ordenacao_simples(lista), [1, 2, 4, 6, 8, 10])


if __name__ == '__main__':
    unittest.main()
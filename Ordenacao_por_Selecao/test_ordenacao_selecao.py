import unittest
from ordenacao_selecao import *


class TestOrdenacaoSelecao(unittest.TestCase):

    def test_case_a(self):
        lista = [5, 3, 6, 2, 10]
        self.assertEqual(ordenacao_por_selecao(lista), [2, 3, 5, 6, 10])

    def test_case_b(self):
        lista = [1, 2, 3, 4, 5]
        self.assertEqual(ordenacao_por_selecao(lista), [1, 2, 3, 4, 5])

    def test_case_c(self):
        lista = [1002, 70, 20, 6, 228, 40]
        self.assertEqual(ordenacao_por_selecao(lista), [6, 20, 40, 70, 228, 1002])

if __name__ == '__main__':
    unittest.main()        
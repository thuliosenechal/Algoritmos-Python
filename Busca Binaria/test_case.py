import unittest
from busca_binaria import busca_binaria


class TestBuscaBinaria(unittest.TestCase):

    def test_case_8(self):
        lista = range(9)
        self.assertEqual(busca_binaria(lista, 8), 3)

    def test_case_128(self):
        lista = range(129)
        self.assertEqual(busca_binaria(lista, 128), 7)

    def test_case_1024(self):
        lista = range(1025)
        self.assertEqual(busca_binaria(lista, 1024), 10)

    def test_false(self):
        lista = range(9)
        self.assertFalse(busca_binaria(lista, 10))

    def test_none(self):
        lista = range(10)
        self.assertIsNone(busca_binaria(lista, 12))

if __name__ == '__main__':
    unittest.main()        
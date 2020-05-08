import unittest

from busca_binaria import busca_binaria


class TestBuscaBinaria(unittest.TestCase):
    
    def test_case_a(self):
        lista = [0, 11, 21, 33, 45, 45, 61, 71, 72, 73]
        num_procurado = 33
        self.assertEqual(busca_binaria(lista, num_procurado), 3)

    def test_case_b(self):
        lista = [1, 2, 3, 4, 5]
        num_procurado = 3
        self.assertEqual(busca_binaria(lista, num_procurado), 2)

    def test_case_c(self):
        lista = [1, 2, 3, 4, 5]
        num_procurado = 20
        self.assertEqual(busca_binaria(lista, num_procurado), None)

    def test_case_d(self):
        lista = [1, 2, 3, 4, 6]
        num_procurado = 5
        self.assertFalse(busca_binaria(lista, num_procurado), None)

if __name__ == '__main__':
    unittest.main()        
import unittest

from quicksort import quicksort


class TestQuicksort(unittest.TestCase):
    
    def test_numeros(self):
        lista = [10, 4, 6, 5, 3, 2, 16, 18, 12]
        self.assertEqual(quicksort(lista), [2, 3, 4, 5, 6, 10, 12, 16, 18])

    def test_palavras(self):
        lista = ['italia', 'brasil', 'portugal', 'argentina']
        self.assertEqual(quicksort(lista), ['argentina', 'brasil', 'italia', 'portugal'])

if __name__ == '__main__':
    unittest.main()
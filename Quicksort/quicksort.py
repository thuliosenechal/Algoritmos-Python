'''
O(n²) no pior caso
O(n*log(n)) no caso médio

'''

def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menores = [i for i in lista[1:] if i <= pivo]
        maiores = [i for i in lista[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

if __name__ == '__main__':
    print(quicksort([10, 4, 6, 5, 3, 2, 16, 18, 12]))
    print(quicksort(['italia', 'brasil', 'portugal', 'argentina']))
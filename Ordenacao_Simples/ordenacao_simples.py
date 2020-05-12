'''
O(n)

'''

def ordenacao_simples(lista):
    for i in range(len(lista) -1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

if __name__ == '__main__':
    lista = [3, 2, 9, 5, 1, 4]
    print(ordenacao_simples(lista))
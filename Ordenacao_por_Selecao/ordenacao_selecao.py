'''
O(n²)

Algoritmo lento de ordenação 
'''
def busca_menor_numero(lista):
    menor = lista[0]
    menor_indice = 0
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            menor_indice = i
    return menor_indice


def ordenacao_por_selecao(lista):
    nova_lista = []
    for i in range(len(lista)):
        menor_indice = busca_menor_numero(lista)
        nova_lista.append(lista.pop(menor_indice))
    return nova_lista

if __name__ == '__main__':
    print(ordenacao_por_selecao([5, 3, 6, 2, 10]))
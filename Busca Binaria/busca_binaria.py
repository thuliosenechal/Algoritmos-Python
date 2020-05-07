
lista = range(129)
num_procurado = 128

def busca_binaria(lista, num_procurado):
    indice_menor_num = 0
    indice_maior_num = len(lista) - 1
    count = 0

    while indice_menor_num <= indice_maior_num:
        indice_meio_da_lista = (indice_menor_num + indice_maior_num) // 2
        chute = lista[indice_meio_da_lista]

        if num_procurado == chute:
            return indice_meio_da_lista
        elif num_procurado > chute:
            indice_menor_num = indice_meio_da_lista + 1
        else:
            indice_maior_num = indice_meio_da_lista - 1
        
        count += 1

    return None

if __name__ == '__main__':
    print(busca_binaria(lista, num_procurado))

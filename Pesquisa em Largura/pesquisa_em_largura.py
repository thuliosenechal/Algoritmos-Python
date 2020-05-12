'''

O tempo de execução é no mínimo O(Número de arestas)
Além disso será mantida uma lista com as pessoas já verificadas, que é O(1).
Fazer isso para cada pessoa terá o tempo de O(Número de pessoas)

Portanto, o tempo de execução de pesquisa em largura é 
O(Número de pessoas + número de arestas), que é frequentemente escrito como:

O(V + A)

V = Número de vértices
A = Número de arestas

Exemplo retirado do livro: Entendendo Algoritmos - Aditya Y. Bhargava
Abaixo temos um pequeno, simples e aleatório exemplo onde procuramos um 
vendedor de manga dentre uma rede de pessoas como uma rede de amigos do
facebook, por exemplo, onde temos nossos amigos, amigos dos nossos amigos,
e assim por diante.

O critério para ser o vendedor de manga é que a ultima letra do nome tem que 
terminar com a letra 'm'.

'''

from collections import deque


grafo = {}
grafo['voce'] = ['alice', 'bob', 'claire']
grafo['bob'] = ['anuj', 'peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['thom', 'jonny']
grafo['anuj'] = []
grafo['peggy'] = []
grafo['thom'] = []
grafo['jonny'] = []


def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'


def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + ' é um vendedor de manga!')
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False


pesquisa('voce')
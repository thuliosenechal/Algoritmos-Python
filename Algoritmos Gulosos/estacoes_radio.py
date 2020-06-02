'''
Algotirmo Guloso ou Algoritmo de Aproximação

O(n^2), em que n é o número de estações de rádio no exemplo abaixo.


No cenário abaixo temos um exemplo onde há várias estações de rádio
disponíveis em vários estados dos EUA.

O desafio é fazer com que um programa de rádio atinja em todos os 50 
estados americanos.

É necessário decidir em quais estações transmitir para atingir todos os
ouvintes. Porém transmitir em diferentes estações tem um custo, e nós
estamos tentando minimizar o número de estações nas quais nós 
transmitimos para minimizar o custo.

Lista de estações:

Estação de rádio | Estados disponíveis
    Kum                 ID, NV, UT
    Kdois               WA, ID, MT
    Ktres               OR, NV, CA
    Kquatro             NV, UT
    Kcinco              CA, AZ



'''

estados_abranger = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

estacoes = {}
estacoes['kone'] = set(['id', 'nv', 'ut'])
estacoes['ktwo'] = set(['wa', 'id', 'mt'])
estacoes['kthree'] = set(['or', 'nv', 'ca'])
estacoes['kfour'] = set(['nv', 'ut'])
estacoes['kfive'] = set(['ca', 'az'])

estacoes_finais = set()

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()

    for estacao, estados_por_estacao in estacoes.items():
        cobertos = estados_abranger & estados_por_estacao

        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos

    estados_abranger -= estados_cobertos
    estacoes_finais.add(melhor_estacao)
        
print(f'Estacoes_finais: {estacoes_finais}')

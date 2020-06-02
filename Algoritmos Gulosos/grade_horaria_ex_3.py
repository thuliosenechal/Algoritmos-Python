'''
Algoritmos Gulosos ou Algoritmos de aproximação

São algoritmos onde não se tem uma solução rápida ou a solução
mais eficaz. 

No exemplo abaixo temos uma grade de horários de aulas para uma
unica sala de aula, onde alguns horários conflitam com outros
horários.

Ex: Aula de artes é entre as 09:00 e 10:00 e a aula de ingles
é entre 09:30 e 10:30. Como é apenas uma sala de aula, fica
impossível ter essas duas aulas no mesmo horário.

Pensando nisso, temos que criar um algoritmo onde se cria uma
grade de horários que se encaixem e não se conflitam.

É de se esperar que nem todos os horários permanecerão na 
grade horária final, tendo assim que abrir mão de algumas 
matérias.

No exemplo, não utilizei o formato de horário convencional pois
a intenção é mostrar o algoritmo funcionando, e com isso
utilizei para o .3 para informar que é metade de uma hora

Ex: 09:30 -> 9.3


Nesse exemplo, os horários estão dispostos fora de ordem de horário,
e com isso uma função de ordenação simples para sortear pelo
horário de início das aulas e ficar conforme no arquivo do ex 1.


Temos mais 2 outros arquivos simulando outras formas de 
disposição de horários

O resultado do algoritmos significa que não foi possível criar
uma grade que contemplasse todos os horários porém foi criado
uma grade onde coubesse o maior número de matérias no formato
em que nos foi entregue.

O resultado será:

{'materia': 'artes', 'inicio': 9, 'fim': 10}
{'materia': 'matematica', 'inicio': 10, 'fim': 11}
{'materia': 'musica', 'inicio': 11, 'fim': 12}

'''


aulas = [{'materia': 'matematica', 'inicio': 10, 'fim': 11},
         {'materia': 'musica', 'inicio': 11, 'fim': 12},
         {'materia': 'artes', 'inicio': 9, 'fim': 10},
         {'materia': 'ingles', 'inicio': 9.3, 'fim': 10.3},
         {'materia': 'cc', 'inicio': 10.3, 'fim': 11.3}]
      

def ordenar_aulas(lista):
    for i in range(len(lista) -1):
        for j in range(i+1, len(lista)):
            if lista[i]['fim'] > lista[j]['fim']:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def organizar_aulas(lista):
    menor_horario = 0
    nova_grade = []

    for aula in lista:
        inicio_aula = aula['inicio']
        fim_aula = aula['fim']
        
        if inicio_aula >= menor_horario and fim_aula >= menor_horario:
            menor_horario = fim_aula
            nova_grade.append(aula)
        else:
            continue
    
    return nova_grade


lista = ordenar_aulas(aulas)
grade_horaria = organizar_aulas(lista)

for horario in grade_horaria:
    print(horario)
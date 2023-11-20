#combinação de funções
from random import randint

lista = list()

def rando():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(0, 10))
        print(f'{lista[c]}', end=' ')


def soma():
    s = 0
    for a in lista:
        if a % 2 == 0:
            s += a
    print(f'\nSomando apenas os valores pares de {lista}, temos {s}.')


#main program
rando()

soma()

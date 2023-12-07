from random import randint
from time import sleep
from operator import itemgetter
resultado = dict()
ranking = list()
for c in range(0,4):
    valor = randint(1,6)
    nome = (f"{'jogador'}{c+1}")
    resultado[nome] = valor
print('Valores sorteados:')
for k, v in resultado.items():
    print(f"   O {k} tirou {v} no dado.")
    sleep(1)
ranking = sorted(resultado.items(), key=itemgetter(1),reverse=True)
print('Os vencedores foram:')
p=0
for j in ranking:
    p+=1
    print(f'{p}º lugar: {j[0]} com {j[1]}.')
    sleep(1)

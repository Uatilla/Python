from random import randint
from time import sleep
jogo=list()
print('-'*30)
print(f"{'JOGOS MEGA-SENA':^30}")
print('-'*30)
qtd = int(input('Quantos jogos você quer eu sorteie? '))
print(f"SORTEANDO {qtd:^5} JOGOS:")
for c in range(0, qtd):
    sleep(0.5)
    for j in range(0, 6):
        n = randint(0, 60)
        while n in jogo:
            n = randint(0, 60)
        jogo.append(n)
    jogo.sort()
    print(f'Jogo {c+1}: {jogo}')
    jogo.clear()
print('BOA SORTE!')


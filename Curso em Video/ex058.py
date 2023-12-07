from random import randint
from time import sleep
print('--- Advinhe o número selecionado pelo computador ---')
num = randint(0, 10)
esc = ''
rep=0
while num != esc:
    esc = int(input('Digite um número inteiro entre 0 e 10: '))
    print('VERIFICANDO...')
    sleep(0.5)
    if num == esc:
        print('Parabens! Você acertou! O número sorteado foi o número {}.'.format(num))
        rep += 1
    else:
        print('Errou, tente novamente!')
        rep += 1
print('Foram necessário {} palpites para acertar.'.format(rep))
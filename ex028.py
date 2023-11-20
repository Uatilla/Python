from random import randint
from time import sleep
print('--- Advinhe o número selecionado pelo computador ---')
num = randint(0,5)
esc = int(input('Digite um número inteiro entre 0 e 5: '))
print('VERIFICANDO...')
sleep(3)
if num == esc:
    print('Parabens! Você acertou o número!')
else:
    print('Errou, tente novamente o número escolhido pelo computador foi {}'.format(num))

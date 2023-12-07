# DESEMPACOTAMENTO DE PARÂMETROS
from time import sleep
def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for p in num:
        print(f'{p}', end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        valor = 0
    else:
        valor = max(num)
    print(f'O maior valor informado foi {valor}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

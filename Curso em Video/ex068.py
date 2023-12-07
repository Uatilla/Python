from random import randint
print('-='*30)
print('Escolha um número para jogar PAR ou IMPAR comigo!')
print('-='*30)
contador = 0
while True:
    núm = int(input('Digite um número: '))
    pc = randint(0,10)
    op = ' '
    while op not in 'PI':
        op = str(input('Par ou Impar [P/I]: ')).upper().strip()[0]
    print('-=' * 30)
    total = núm + pc
    if total % 2 == 0:
        print(f'Você jogou {núm}, o computador jogou {pc}. A soma total foi {total} o número é PAR.')
        resultado = 'P'
    else:
        print(f'Você jogou {núm}, o computador jogou {pc}. A soma total foi {total} o número é IMPAR.')
        resultado = 'I'
    if op == resultado:
        print('Você acertou!')
        print('Vamos jogar novamente...')
        print('-=' * 30)
        contador +=1
        continuar = 'S'
    else:
        print('Você errou!')
        continuar == 'N'
        break
print(f'Você acertou {contador} vezes.')
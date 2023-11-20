from time import sleep
def contador():
    print('-='*30)
    print('Contagem de 1 até 10, de 1 em 1.')
    for v in range(1,11,1):
        print(v, end=' ')
        sleep(0.2)
    print('FIM!')
    print('-=' * 30)
    print('Contagem de 10 até 0, de 2 em 2.')
    for h in range(10,-1,-2):
        print(h, end=' ')
        sleep(0.2)
    print('FIM!')
    print('-=' * 30)


# CONTADOR PERSONALIZADO
def contadorpers():

    if f<i and p>0:
        print(f'Contagem de {i} até {f}, de {p} em {p}.')
        for v in range(i, f-1, -p):
            print(v, end=' ')
            sleep(0.2)
    elif f<i and p<0:
        print(f'Contagem de {i} até {f}, de {p*-1} em {p*-1}.')
        for v in range(i, f - 1, p):
            print(v, end=' ')
            sleep(0.2)
    elif f>i and p<0:
        print(f'Contagem de {i} até {f}, de {p} em {p}.')
        for v in range(i, f+1, -p):
            print(v, end=' ')
            sleep(0.2)
    elif f>i and p>0:
        print(f'Contagem de {i} até {f}, de {p} em {p}.')
        for v in range(i, f+1, p):
            print(v, end=' ')
            sleep(0.2)
    elif f>i and p<0:
        print(f'Contagem de {i} até {f}, de {p*-1} em {p*-1}.')
        for v in range(i, f+1, p*-1):
            print(v, end=' ')
            sleep(0.2)
    elif f<i and p==0:
        print(f'Contagem de {i} até {f}, de 1 em 1.')
        for v in range(i, f-1, -1):
            print(v, end=' ')
            sleep(0.2)
    elif f>i and p==0:
        print(f'Contagem de {i} até {f}, de 1 em 1.')
        for v in range(i, f+1, 1):
            print(v, end=' ')
            sleep(0.2)
    print('FIM!')
    print('-=' * 30)


# MAIN PROGRAM
contador()
print('Agora é sua vez de personalizar a contagem!')
i = int(input('INÍCIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
contadorpers()

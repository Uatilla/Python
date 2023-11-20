núm = 0
while True:
    cont = 0
    núm = int(input('Quer ver a tabuada de qual valor: '))
    if núm < 0:
        break
    print(40*'-')
    while cont < 10:
        cont += 1
        resultado = cont * núm
        print(f'{núm} x {cont} = {resultado}')
    print(40 * '-')
print('Programa de tabuada encerrado, VOLTE SEMPRE!')
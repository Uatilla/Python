lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor duplicado! Não vou adicionar...')

    cont = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Opção inválida! Quer continuar? [Sim ou Não]: ')).upper().strip()[0]
    if cont == 'N':
        break
print('-='*30)
lista.sort()
print(f'Você digitou os valores:  {lista}')

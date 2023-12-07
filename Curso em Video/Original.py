lista = []
pares = []
impar = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impar.append(valor)
    continuar = str(input('Continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [Sim ou Não]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Lista digitada: {lista}')
print(f'Valores pares: {pares}')
print(f'Valores impares: {impar}')
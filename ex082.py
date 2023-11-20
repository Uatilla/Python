lista = []
pares = []
impar = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    continuar = str(input('Continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [Sim ou Não]: ')).upper().strip()[0]
    if continuar == 'N':
        break
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impar.append(v)
print('-='*30)
print(f'Lista digitada: {lista}')
print(f'Valores pares: {pares}')
print(f'Valores impares: {impar}')
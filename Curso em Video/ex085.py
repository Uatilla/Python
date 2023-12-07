listageral=[[],[]]
for c in range(0,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        listageral[0].append(valor)
    else:
        listageral[1].append(valor)
listageral[0].sort()
listageral[1].sort()
print(f'Valores pares: {listageral[0]}.')
print(f'Valores Impares: {listageral[1]}.')

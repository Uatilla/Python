tupla = (int(input('Digite o 1º valor: ')), int(input('Digite o 2º valor: ')),
         int(input('Digite o 3º valor: ')), int(input('Digite o 4º valor: ')))
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
if 3 not in tupla:
    print('O número três não aparece na lista!')
else:
    print(f'O número três aparece na {tupla.index(3)+1}ª posição.')
for n in tupla:
    if n % 2 == 0:
        print(f'O valores pares são: {n}', end=' ')
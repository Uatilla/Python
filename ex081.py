lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida! Deseja continuar? [Sim ou Não]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-='*30)
lista.sort(reverse=True)
print(f'A lista apresenta {len(lista)} elementos.')
print(f'A lista ordenada de maneira decrescente: {lista}.')
if 5 in lista:
    print(f'O valor 5 foi digitado nas posições: ', end='')
    for x, v in enumerate(lista):
        if v == 5:
            print(f'{x}...',end=' ')
else:
    print('O valor 5 não foi encontrado!')

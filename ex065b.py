
lista = []
continuar = 's'
while continuar == 's':
    num = int(input('Digite um número: '))
    lista = lista + [num]
    continuar = str(input('Você quer continuar? [S/N]: ')).lower().strip()[0]
media = sum(lista)/len(lista)
print('O maior valor foi: {}'. format(max(lista)))
print('O menor valor foi: {}'. format(min(lista)))
print('A média foi: {:.2f}'. format(media))
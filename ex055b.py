lista = []
for p in range (1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    lista = lista + [peso]
print('O maior peso foi {}Kg'. format(max(lista)))
print('O menor peso foi {}Kg'. format(min(lista)))
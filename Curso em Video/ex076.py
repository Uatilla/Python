tupla_produtos = ('Lápis', 1.75,
                  'Borracha',2.00,
                  'Caderno',15.90,
                  'Estojo',25.00,
                  'Transferidor',4.20,
                  'Compasso',9.99,
                  'Mochila',120.32,
                  'Canetas',22.30,
                  'Livro',34.90)
print('-'*40)
print('{: ^40}'.format('LISTA DE PRODUTOS'))
print('-'*40)
for pos in range(0, len(tupla_produtos)):
    if pos % 2 == 0:
        print(f'{tupla_produtos[pos]:.<30}', end='')
    else:
        print(f'R${tupla_produtos[pos]:>7.2f}')
print('-'*40)
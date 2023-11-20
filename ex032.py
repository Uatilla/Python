ano = int(input('Digite um ano: '))
if ano % 4 == 0
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('É ano bissexto.')
        else:
            print ('Não é ano bissexto.')
    else:
        print('É ano bissexto.')
else:
    print('Não é ano bissexto.')
dist = float(input('Qual a distância da viagem: '))
if dist > 200:
    print('O valor da viagem será : R${:.2f}'.format(dist*0.45))
else:
    print('O valor da viagem será: R${:.2f}'.format(dist*0.5))

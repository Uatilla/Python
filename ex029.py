velocidade = float(input('Digite a velocidade atual em Km/h: '))
multa = (velocidade-80)*7
if velocidade > 80:
    print('Você foi multado em R${:.2f}, por ultrapassar o limite de velocidade de 80Km/h.'.format(multa))
else:
    print('Parabéns, você está dentro do limite de velocidade.')

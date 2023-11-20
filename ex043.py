peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso/(altura*altura)
if imc<18.5:
    print('Seu IMC é de {:.2f}, você está ABAIXO DO PESO.'.format(imc))
elif imc <= 25:
    print('Seu IMC é de {:.2f}, você está com o PESO IDEAL.'.format(imc))
elif imc <= 30:
    print('Seu IMC é de {:.2f}, você está com SOBREPESO'.format(imc))
elif imc <= 40:
    print('Seu IMC é de {:.2f}, você está com OBESIDADE.'.format(imc))
else:
    print('Seu IMC é de {:.2f}, você está com OBESIDADE MÓRBIDA.'.format(imc))
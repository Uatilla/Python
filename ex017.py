from math import hypot,floor
n1 = float(input('Qual o valor do cateto oposto em cm: '))
n2 = float(input('Qual o valor do cateto adjacente em cm: '))
print('O valor da hipotenusa, será aproximadamente de: {:.2f}cm'.format(hypot(n1,n2)))

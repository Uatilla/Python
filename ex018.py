from math import cos,sin,tan,radians
a = float(input('Digite um angulo: '))
num = radians(a)
print('Do ângulo de {}, temos o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}'.format(a,sin(num),cos(num),tan(num)))

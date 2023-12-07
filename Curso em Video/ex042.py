print('Vamos verificar se essas retas podem formar um triangulo?')
x = float(input('Digite o primeiro lado do triângulo: '))
y = float(input('Digite o segundo lado do triângulo: '))
z = float(input('Digite o terceiro lado do triângulo: '))

if (x+y)>z:
    if (x+z)>y:
        if (y+z)>x:
           if x == y == z:
               print('Os lados {}, {} e {}, podem formar um triângulo, e é uma triangulo Equilátero'.format(x, y, z))
           elif x != y != z:
               print('Os lados {}, {} e {}, podem formar um triângulo, e é uma triangulo Escaleno'.format(x, y, z))
           else:
               print('Os lados {}, {} e {}, podem formar um triângulo, e é uma triangulo Isósceles'.format(x, y, z))
        else:
            print('Os lados informados não podem formar um triângulo')
    else:
        print('Os lados informados não podem formar um triângulo')
else:
    print('Os lados informados não podem formar um triângulo')

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
final = int(input('Digite quantos termos da fibonacci gostaria de ver: '))
x = 0
y = 1
print('~'*30)
print('{} > {}'.format(x, y),end='')
z = x + y
t=2
while t < final:
    print(' > {}'.format(z),end='')
    x = y
    y = z
    z = x + y
    t +=1
print(' > Fim')
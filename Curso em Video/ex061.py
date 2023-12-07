p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da progressão: '))
t=0
while t < 10:
    print(p, end=', ')
    t +=1
    p = p+r
print('Fim')

p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da progressão: '))
for c in range (p,(p+10*r),r):
    print(c,end=', ')
print('Fim')
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da progressão: '))
t=0
limite = 10
while t < limite:
    print(p, end=', ')
    t +=1
    p = p+r
acrescimo = int(input('Quantos quer adicionar: '))
while acrescimo != 0:
    t = 0
    while t < acrescimo:
        print(p, end=', ')
        t += 1
        p = p + r
    acrescimo = int(input('Quantos quer adicionar: '))



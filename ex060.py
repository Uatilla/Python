num = int(input('Digite um número: '))
fatorial = num-1
inc = num
while fatorial > 0:
    num = num*fatorial
    fatorial = fatorial -1
print('O resultado de {}! é: {}.'.format(inc, num))

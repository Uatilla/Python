núm = int(input('Digite um número: '))
tot = 0
for c in range(1,núm+1):
    if núm % c == 0:
        tot = tot + 1
    print('{} '.format(c), end='')
print('\nO número {} foi divisível {} vezes'.format(núm,tot))
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por iso ele NÃO É PRIMO!')

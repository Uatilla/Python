('--- BEM VINDO AO CONVERSOR DE BASES ---')
print('--- ESCOLHA ABAIXO A OPÇÃO DESEJADA ---')
num = int(input('Digite o valor a ser convertido: '))
print('[1] - HEXADECIMAL')
print('[2] - OCTAL')
print('[3] - BINARIA')
op = int(input('Digite a opção desejada: '))
bin = bin(num)
hex = hex(num)
oct = oct(num)
if op == 1:
    print('Do valor {} o equivalente Hexadecimal será: {}'.format(num,hex[2:]))
elif op == 2:
    print('Do valor {} o equivalente Octal será: {}'.format(num,oct[2:]))
elif op == 3:
    print('Do valor {} o equivalente Binário será: {}'.format(num,bin[2:]))
else:
    print('Opção informada, inválida!')
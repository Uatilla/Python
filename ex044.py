('--- CALCULADORA DE DESCONTOS ---')
print('--- ESCOLHA ABAIXO A OPÇÃO DESEJADA ---')
num = float(input('Digite o valor da venda: '))
print('[ 1 ] - À VISTA (DINHEIRO OU CHEQUE)')
print('[ 2 ] - À VISTA (CARTÃO)')
print('[ 3 ] - 2X NO CRÉDITO')
print('[ 4 ] - 3X OU MAIS NO CRÉDITO')
print('------------------------------------------\n')
op = int(input('Digite a opção desejada: '))
if op == 1:
    print('O valor final a ser pago com desconto de 10% será: {}'.format(num*0.9))
elif op == 2:
    print('O valor final a ser pago com desconto de 5% será: {}'.format(num*0.95))
elif op == 3:
    print('O valor final a ser pago não sofrerá alterações: {}'.format(num))
elif op == 4:
    print('O valor final a ser pago terá acréscimo de 20%, totalizando: {}'.format(num*1.2))
else:
    print('Opção informada, inválida!')
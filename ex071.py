notas50 = notas20 = notas10 = 0
print('='*20)
print ('BANK OF AMERICA')
print('='*20)
saque = int(input('Qual valor você quer sacar? R$'))
notas50 = saque // 50
saldo = saque - (50 * notas50)
notas20 = saldo // 20
saldo = saldo - (20*notas20)
notas10 = saldo // 10
saldo = saldo - (10*notas10)
print(f'Total de {notas50} cédulas de R$50')
print(f'Total de {notas20} cédulas de R$20')
print(f'Total de {notas10} cédulas de R$10')
print(f'Total de {saldo} cédulas de R$1')
print('='*30)
print('HAVE A GOOD DAY!')

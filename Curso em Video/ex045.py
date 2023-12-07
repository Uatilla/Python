import random
print('--- BEM VINDO AO JOKENPÔ ---')
print('PEDRA')
print('PAPEL')
print('TESOURA')
op = str(input('Jogador digite uma opção acima: ').lower())
lista = ['PEDRA', 'PAPEL', 'TESOURA']
esc = random.choice(lista)
if op == 'pedra' and esc == 'TESOURA' or op == 'papel' and esc == 'PEDRA' or op == 'tesoura' and esc == 'PAPEL':
    print('Parabéns!!! Você venceu, eu escolhi {} e você {}.'.format(esc, op.upper()))
elif op == 'pedra' and esc == 'PAPEL' or op == 'papel' and esc == 'TESOURA' or op == 'tesoura' and esc == 'PEDRA':
    print('HAHAHA EU VENCI, eu escolhi {} e você {}.'.format(esc, op.upper()))
elif op == 'pedra' and esc == 'PEDRA' or op == 'papel' and esc == 'PAPEL' or op == 'tesoura' and esc == 'TESOURA':
    print('NINGUEM VENCEU, nós dois escolhemos {}.'.format(esc, op.upper()))
else:
    print('Opção informada inválida!')


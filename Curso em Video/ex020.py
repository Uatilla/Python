from random import sample,shuffle
n1 = str(input('1ª Aluno: '))
n2 = str(input('2º Aluno: '))
n3 = str(input('3º Aluno: '))
n4 = str(input('4ª Aluno: '))
seq = [n1, n2, n3, n4]
'''print('A ordem de apresentação será: {}'.format(sample(seq,4)))'''
shuffle(seq)
print('A ordem de apresentação será: ')
print(seq)


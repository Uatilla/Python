média = 0
idademaisvelho = 0
nomemaisvelho = ''
menosque20 = 0
for p in range(1,5):
    print('----------- Dados da {}ª pessoa -----------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M ou F): ').lower().strip())
    média += idade
    if sexo == 'm':
        if idade > idademaisvelho:
            idademaisvelho = idade
            nomemaisvelho = nome
    elif sexo == 'f':
        if idade < 20:
            menosque20 += 1
média = média/p
print('\n==============================================================')
print('SEGUE ANÁLISE DOS DADOS INFORMADOS')
print('==============================================================\n')
print('A idade média da população é de {:.0f} ANOS'. format(média))
if idademaisvelho == 0:
    print('Não foram identificados homens dentro da população informada.')
else:
    print('{} é o homem mais velho com {} anos de idade'. format(nomemaisvelho,idademaisvelho))
if menosque20 == 0:
    print('Não foram identificadas mulheres dentro da população informada.')
else:
    print('{} mulheres possuem idade menor que 20 anos.'.format(menosque20))
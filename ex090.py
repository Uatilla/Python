aluno= dict()
aluno['Nome'] =str(input('Nome: ')).strip()
aluno['Média'] = float(input('Média: '))
if aluno['Média'] < 7:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Aprovado'
print('-='*12)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')


lista_geral = []
aluno = []
notas = []

while True:
    #Entrada das notas e do nome do aluno.
    nome = str(input('Nome: '))
    aluno.append(nome)
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med = (n1+n2)/2
    #Adição das entrada nas listas de suporte e lista principal.
    notas.append(n1)
    notas.append(n2)
    notas.append(med)
    aluno.append(notas[:])
    lista_geral.append(aluno[:])
    aluno.clear()
    notas.clear()
    continuar = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida! Quer continuar? [Sim ou Não]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*14)
print(f"{'Nº':<3}",end='')
print(f"{'NOME':<15}",end='')
print(f"{'MÉDIA':<10}")
print('-'*28)
#print dos dados lançados em forma de tabela.
for c, v in enumerate(lista_geral):
    print(f'{c:<3}{v[0]:<15}{v[1][2]:<10}')
print('-'*28)
#Consulta dos dados lançados.
while True:
    num = int(input('Mostrar notas de qual aluno(a)? '))
    while num >= len(lista_geral) or num < 0:
        num = int(input('Número inválido! Deseja mostrar notas de qual aluno(a)? '))
    print(f'As notas do(a) aluno(a) {lista_geral[num][0]} são {lista_geral[num][1][0]} e {lista_geral[num][1][1]}')
    cont = str(input('Você quer continuar a consulta? [S/N]: ')).strip().upper()[0]
    while cont not in 'SN':
        cont = str(input('Opção inválida! Quer continuar? [Sim ou Não]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('MUITO OBRIGADO, VOLTE SEMPRE!')
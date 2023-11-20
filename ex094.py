# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
lista = list()
pessoa = dict()
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo inválido! Digite [M/F]:')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Inválido!, Deseja continuar? [Sim ou Não]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(lista)} pessoas.')
soma = 0
for c in range(0, len(lista)):
    soma += lista[c]['idade']
media = soma/len(lista)
print(f'A média da idade do grupo é de {media} anos de idade.')
print('Mulheres cadastradas:')
for f in lista:
    if f['sexo'] == 'F':
        print(f"{f['nome']} com {f['idade']} anos de idade.")
print(f'A média de idade foi de {media} anos de idade, as seguintes pessoas estão acima da média:')
for f in lista:
    if f['idade'] >= media:
        print(f"{f['nome']} é do sexo {f['sexo']} e possui {f['idade']} anos de idade.")
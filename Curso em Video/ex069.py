cont = maiorid = homens = mulheressub20 = 0
print('-'*30)
print('CADASTRE UM PESSOA')
print('-'*30)
while True:
    idade = int(input('Qual a idade: '))
    sexo = str(input('Qual o sexo: [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        if sexo in 'MF':
            break
        else:
            sexo = str(input('Qual o sexo: [M/F]: ')).upper().strip()[0]
    if idade > 18:
        maiorid += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheressub20 += 1
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-' * 30)
print(f'Foram cadastrados {maiorid} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {homens} homens.')
print(f'Foram cadastrados {mulheressub20} mulheres com idade inferior a 20 anos.')
print('*'*30)
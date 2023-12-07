sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'FM':
        sexo = str(input('Dados inválidos. Informe seu sexo [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo Masculino registrado com sucesso!')
else:
    print('Sexo Feminino registrado com sucesso!')
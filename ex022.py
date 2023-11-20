nome = str(input('Qual o seu nome? ').strip())
print('O nome em maísculo é: {}'.format(nome.upper()))
print('O nome em minúsculo é: {}'.format(nome.lower()))
print('O comprimento total é de: {}'.format(len(nome.replace(' ',''))))
print('O primeiro nome é: {} e tem comprimento de {} caractéres.'.format(nome.split()[0],len(nome.split()[0])))



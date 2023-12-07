cidade = str(input('Digite o nome de uma cidade: ')).strip()
alfa = cidade.lower()
print('Na cidade {}, existe Santo no início?: {}.'.format(cidade,'santo'in alfa.split()[0]))


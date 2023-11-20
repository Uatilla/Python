from datetime import datetime
ano_atual = datetime.now().year
funcionario = dict()
funcionario['Nome']=str(input('Digite o nome: ')).strip()
funcionario['Nascimento'] = int(input('Ano de nascimento: '))
funcionario['CTPS'] = int(input('Nº da CTPS (0 não tem): '))
funcionario['Idade'] = ano_atual - funcionario['Nascimento']
if funcionario['CTPS'] != 0:
    funcionario['Contratação'] = int(input('Ano de contratação: '))
    funcionario['Salario'] = float(input('Salário: R$'))
    funcionario['Aposentadoria'] = 35 - (ano_atual - funcionario['Contratação']) + funcionario['Idade']
print('-='*30)
print(f"{funcionario['Nome']} tem {funcionario['Idade']} anos de idade.")
if funcionario['CTPS'] != 0:
    print(f"O Nº da CTPS é {funcionario['CTPS']}, sendo contratado no ano de {funcionario['Contratação']}.")
    print(f"O atual salário é: {funcionario['Salario']}, irá aposentar com {funcionario['Aposentadoria']} anos de idade.")
else:
    print('Ele não possui CTPS ativa.')
print('OBRIGADO POR CONSULTAR!')
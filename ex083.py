equacao=list()
equacao = str(input('Digite uma expressão matematica: '))
if equacao.count('(')==equacao.count(')'):
    print('Equação válida!')
else:
    print('Equação inválida!')


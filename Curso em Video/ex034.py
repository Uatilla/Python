salario = float(input('Digite o salário: '))
if salario > 1250:
    reajuste = salario*0.1
    print('O valor de reajuste será de R${}, o salário será de R${}'. format(reajuste,salario+reajuste))
else:
    reajuste = salario*0.15
    print('O valor do reajuste será de R${}, o salário será de R${}'.format(reajuste, salario+reajuste))


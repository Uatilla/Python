from time import sleep
print('--- BEM VINDO AO SIMULADOR DA CASA PRÓPRIA ---')
casa = float(input('Digite o valor do imóvel a ser financiado: '))
salario = float(input('Digite o seu salário atual: '))
anos = float(input('Digite em quantos anos você pretende pagar esse imóvel: '))

prestacao = casa/12/anos

print('VERIFICANDO...')
sleep(3)
print('----------------------------------------------------------')
if salario*0.3>prestacao:
    print('O financiamento poderá ser feito')
else:
    print('O financiamento não poderá ser feito, por conta da parcela exceder 30% do salário informado!')
print('O valor da prestação será: {:.2f}'. format(prestacao))

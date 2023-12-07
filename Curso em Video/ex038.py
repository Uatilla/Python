from time import sleep
print('--- BEM VINDO AO COMPARADOR DE VALORES ---')
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
print('VERIFICANDO...')
sleep(1.5)
if v1>v2:
    print('O primeiro valor é maior!')
elif v2>v1:
    print('O segundo valor é maior!')
else:
    print('Os valores são iguais!')
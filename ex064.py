num = soma = qtd = 0
num = int(input('Digite um número [999 p/ parar]: '))
while num != 999:
    soma += num
    qtd += 1
    num = int(input('Digite um número [999 p/ parar]: '))
print('Foram digitados {} valores, com a soma de {}.'.format(qtd,soma))
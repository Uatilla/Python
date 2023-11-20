print('-'*30)
print('{:-^30}'.format('CADASTRO DE VENDAS'))
print('-'*30)
lista = []
menorpreço = contador = contadorp = soma = prodbarato = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = int(input('Preço do produto: R$'))
    if contadorp == 0:
        menorpreço = preço
        prodbarato = produto
    if preço < menorpreço:
        menorpreço = preço
        prodbarato = produto
    if preço > 1000:
        contador += 1
        lista = lista + [produto]
    soma += preço
    contadorp += 1
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
    print('~' * 30)
print(f'O total da compra foi {soma} reais.')
print(f'O produto {prodbarato} foi o mais barato custando {menorpreço} reais.')
if contador == 0:
    print('Não foram encontrados produtos acima de 1.000 reais.')
else:
    print(f'Os {contador} produtos {lista}, custaram mais de 1000 reais.')
print('~'*30)
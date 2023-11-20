cont = soma = 0
while True:
    núm = int(input('Digite um valor [999 p/ parar]: '))
    if núm == 999:
        break
    soma += núm
    cont += 1
print(f'Foram digitados {cont} números, cujo somatório é {soma}.')
op = 0
print(36 * '=')
print('BEM VINDO A CALCULADORA ONLINE')
print(36 * '=')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
while op != 5:
    print('Digite a opção desejada:')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos Números')
    print('[5] Sair do Programa')
    op = int(input('Opção: '))
    if op == 1:
        result = n1 + n2
        print('Opção selecionada: SOMAR - Resultado: {}'.format(result))
    elif op == 2:
        result = n1 * n2
        print('Opção selecionada: MULTIPLICAR - Resultado: {}'.format(result))
    elif op == 3:
        result = max([n1,n2])
        print('Opção selecionada: MAIOR - Resultado: {}'.format(result))
    elif op == 4:
        print('Informe os números novamente')
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    elif op == 5:
        print('FINALIZADO...')
    else:
        print('Opção inválida!')

print('Fim do progama')

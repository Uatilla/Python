# Função que calcula a área de um terreno.
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# MAIN PROGRAM
print(f'{"CONTROLE DE TERRENOS":^30}')
print('-' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)

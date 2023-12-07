altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
print('Lembrando que cada litro de tinta cobre uma área de 2m², serão necessários {:.2f} litros de tinta para cobrir a área de {:.2f} metros²'.format(area/2,area))

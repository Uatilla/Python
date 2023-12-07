num = input('Digite um número: ')
n=str(num)
"""print('Unidades: {}'.format(n[3]))
print('Dezenas: {}'.format(n[2]))
print('Centenas: {}'.format(n[1]))
print('Milhares: {}'.format(n[0]))"""
print('___________________________')
n2 = int(num)
nm=n2//1000
nc=(n2-(nm*1000))//100
nd=(n2-((nm*1000)+(nc*100)))//10
nu=(n2-((nm*1000)+(nc*100)+(nd*10)))
print('Unidades: {}'.format(nu))
print('Dezenas: {}'.format(nd))
print('Centenas: {}'.format(nc))
print('Milhares: {}'.format(nm))


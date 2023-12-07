m1 = float(input('Digite a primeira nota: '))
m2 = float(input('Digite a segunda nota: '))
med = (m1+m2)/2
if med<5:
    print('Devido a média ter sido {:.2f}, você está REPROVADO. Estude mais no próximo ano.'.format(med))
elif med<7:
    print('Devido a média ter sido {:.2f}, você está de RECUPERAÇÃO. Estude para a prova final.'.format(med))
else:
    print('Devido a média ter sido {:.2f}, você está APROVADO. PARABÉNS!!'.format(med))
campeonato = ('PALMEIRAS','FLAMENGO','CORINTHIANS','FLUMINENSE','ATHLÉTICO - PR','INTERNACIONAL','ATLÉTICO - MG',
              'AMÉRICA','BRAGANTINO','SANTOS','SÃO PAULO','BOTAFOGO','GOIÁS','CEARÁ','FORTALEZA','CUIABÁ',
              'AVAÍ','CORITIBA','ATLÉTICO - GO','JUVENTUDE')
print(f'G5 PARA A LIBERTADORES: {campeonato[0:5]}')
print('*'*30)
print(f'ZONA DO REBAIXAMENTO: {campeonato[-4:]}')
print('*'*30)
print(f'Lista dos times em ordem alfabetica: {sorted(campeonato)}')
print('*'*30)
chapecoense = campeonato.count('CHAPECOENSE')
if chapecoense == 0:
    print('O CHAPECOENSE não está disputando o campeonato brasileiro da série A deste ano.')
else:
    posicao = campeonato.index('CHAPECOENSE')
    print(f'O CHAPECOENSE está na {posicao}')
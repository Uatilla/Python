populacao = []
individuo = []
pesos = []
while True: # Adicionar os individuos dentro da população.
    individuo.append(str(input('Nome: ')))
    individuo.append(float(input('Peso: ')))
    populacao.append(individuo[:])
    individuo.clear()
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida! Quer continuar? [Sim ou Não]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-='*30)
print(f'Foram cadastradas {len(populacao)} pessoas.')
for p in populacao: # Pegar os pesos da lista população.
    pesos.append(p[1])
print(f'{max(pesos)}Kgs é o maior peso informado. Peso de ',end='')
for p in populacao:
    if p[1] == max(pesos):
        print(f'{p[0]}',end='... ')
print(f'\n{min(pesos)}Kgs é o menor peso informado. Peso de ',end='')
for p in populacao:
    if p[1] == min(pesos):
        print(f'{p[0]}',end='... ')

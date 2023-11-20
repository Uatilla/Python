jogador = dict()
gols = list()
total = 0
jogador['Nome'] = str(input('Nome do Jogador: '))
jogador['Partidas'] = int(input(f"Quantas partidas {jogador['Nome']} fez: "))
for gol in range(0,jogador['Partidas']):
    gols.append(int(input(f'Quantos gols na {gol+1}º partida: ')))
for g in range (0, len(gols)):
    total  += gols[g]
jogador['Gols'] = gols
jogador['Total'] = total
jogador['Aproveitamento'] = total/len(gols)
print('-='*35)
print(f"O jogador {jogador['Nome']} marcou um total de {jogador['Total']} gols nas {jogador['Partidas']} partidas que jogou.")
print(f"A ordem de gols marcados por partida foi {jogador['Gols']} com um aproveitamento de {jogador['Aproveitamento']:.2f}.")
print('-='*35)
print(f"O jogador {jogador['Nome']} jogou {jogador['Partidas']}:")
for j in range(0, jogador['Partidas']):
    print(f" Na partida {j+1}, fez {gols[j]} gols.")

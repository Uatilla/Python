lista_geral = list()
jogador = dict()
lista_gols = list()
saldo_gols = list()
while True:
    jogador['Nome'] = str(input('Nome do Jogador: '))
    jogador['Partidas'] = int(input(f"Quantas partidas {jogador['Nome']} fez: "))
    for gol in range(0, jogador['Partidas']):  # colocar os gols do jogador dentro de uma lista.
        lista_gols.append(int(input(f"Gols na {gol + 1}ª partida: ")))
    saldo_gols = lista_gols[:]
    jogador['Total'] = sum(lista_gols[:])  # somar os gols feitos pelo jogador.
    lista_gols.clear()
    jogador['Gols'] = saldo_gols[:]
    lista_geral.append(jogador.copy())  # copiar o conteúdo do dicionário jogador para a lista geral.
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida! Deseja continuar? [Sim ou Não]: ')).upper().strip()[0]
    print('-' * 60)
    if continuar == 'N':
        break
print('-=' * 30)
print(f"{'Cód.':<6}{'Jogador':<20}{'Gols':<10}{'TOTAL':>10}")
print('-' * 60)
print(lista_geral)
for c in range(0, len(lista_geral)):
    print(f"{c:<5} {lista_geral[c]['Nome']:<20}", end="")
    print(f"{lista_geral[c]['Gols']}", end="")
    print(f"{lista_geral[c]['Total']:>10}")
print('-' * 60)
while True:
    esc = int(input('Detalhar qual jogador? [999 p/ parar]: '))
    if esc == 999:
        break
    while esc > len(lista_geral) - 1:
        esc = int(input('OPÇÃO INVÁLIDA! Detalhar qual jogador? [999 p/ parar]: '))
    print(f"LEVANTAMENTO DO JOGADOR: {lista_geral[esc]['Nome']}")
    for j in range(0, len(lista_geral[esc]['Gols'])):
        print(f"No jogo {j} marcou {lista_geral[esc]['Gols'][j]} gols.")
    print('-'*60)
print('FIM, OBRIGADO PELA CONSULTA!')
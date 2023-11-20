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
    jogador['Gols'] = saldo_gols[:]
    jogador['Total'] = sum(lista_gols[:])  # somar os gols feitos pelo jogador.
    lista_gols.clear()
    lista_geral.append(jogador.copy())  # copiar o conteúdo do dicionário jogador para a lista geral.
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida! Deseja continuar? [Sim ou Não]: ')).upper().strip()[0]
    print('-' * 60)
    if continuar == 'N':
        break
print('-=' * 30)
print(f"{'CÓD.':<6}{'JOGADOR':<15}{'PARTIDAS':<15}{'GOLS':<15}{'TOTAL':<15}")
print('-' * 60)
for k, v in enumerate(lista_geral):
    print(f'{k:<6}',end='') #Seleciona cada elemento dentro da lista maior.
    for d in v.values():
        print(f'{str(d):<15}',end='')#Coloca um espaço de 15 caractéres em cada value de cada dicionário.
    print() #print para pular a linha entre jogadores.
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
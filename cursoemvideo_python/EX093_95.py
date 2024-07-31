gols_list = list()
gols_list_copy = list()
analise = dict()
jogadores = list()


while True:
    jogador = str(input("Qual o nome do jogador?: ")).strip().capitalize()
    jogos = int(input("Quantos jogos ele jogou?: "))

    soma_gols = 0

    for j in range(jogos):
        gols = int(input(f"Quantos gols ele fez no {j+1}° jogo?: "))
        soma_gols += gols
        gols_list.append(gols)
        gols_list_copy = gols_list[:]

    analise = {"jogador": jogador,
                "aproveitamento": gols_list_copy,
                "total_gols": soma_gols}
    
    jogadores.append(analise)

    gols_list.clear()

    continuar = str(input("Quer cadastrar mais um jogador?: [S/N]")).lower().strip()
    if continuar == 'n':
        break
    while continuar != 's' and 'n':
        print('digite uma opção valida: [S/N]')
        continuar = str(input("Quer cadastrar mais um jogador?: [S/N]")).lower().strip()



print("-=" * 30)

print(jogadores)

print("-=" * 30)

print(f'{"Cod":<10} {"Nome":<10} {"Gols":<10} {"Total":<10}')

print("-=" * 30)

for i,v in enumerate(jogadores):
    nome = jogadores[i]['jogador']
    gols = jogadores[i]['aproveitamento']
    total = jogadores[i]['total_gols']

    print(f'{i+1:<10} {nome:<10} {gols} {total:<10}')



while True:
    selecionar = str(input('Quer analisar qual jogador?[999 para parar]: ')).strip().capitalize()

    if selecionar == '999':
        break

    for i, v in enumerate(jogadores):
        if jogadores[i]['jogador'] == selecionar:
            print(jogadores[i]['aproveitamento'])
            gols_list = jogadores[i]['aproveitamento']

            for i, g in enumerate(gols_list):
                print(f"=> Na partida {i+1}, fez {gols_list[i]} gols")
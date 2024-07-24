partidas = list()
gols_list = list()
analise = dict()

soma_gols = 0

jogador = str(input("Qual o nome do jogador?: "))
jogos = int(input("Quantos jogos ele jogou?: "))

for j in range(jogos):
    gols = int(input(f"Quantos gols ele fez no {j+1}° jogo?: "))
    soma_gols += gols
    gols_list.append(gols)

analise = {"jogador": jogador,
            "aproveitamento": gols_list,
            "total_gols": soma_gols}

print("-=" * 30)

print(analise)

print("-=" * 30)

for k, v in analise.items():
    print(f"o campo {k} tem o valor {v} ")

print("-=" * 30)

print(f"o jogador {jogador} jogou {jogos} jogos")

print("-=" * 30)

for i, g in enumerate(gols_list):
    print(f"=> Na partida {i+1}, fez {gols_list[i]} gols")
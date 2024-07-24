from random import randint
from time import sleep



print('VALORES SORTEADOS:')
for j in range(1, 5):
    jogadores  = {'jogador1': f'{randint(1, 6)}',
                'jogador2': f'{randint(1, 6)}',
                'jogador3': f'{randint(1, 6)}',
                'jogador4': f'{randint(1, 6)}',
                }


for k, v in jogadores.items():
    print(f'  {k} tirou {v}')

print(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))

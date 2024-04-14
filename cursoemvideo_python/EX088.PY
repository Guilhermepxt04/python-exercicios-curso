from random import randint
import time

print('-'*30)
print('PALPITES MEGA SENA')
print('-'*30)

mega_sena = list()
palpites = list()

jogos = int(input('Irá jogar quantos jogos?: '))

print('-'*20, end='')
print(f'SORTEANDO {jogos} JOGOS', end='')
print('-'*20)

for j in range(jogos):
    mega_sena.append(palpites[:])

for j in range(jogos):
    for n in range(6):
        while True:
            numero = randint(1, 60)
            if numero not in mega_sena[j]:
                mega_sena[j].append(numero)
            break

for j in range(jogos):
    print(f'{j + 1} JOGO: {mega_sena[j]}')
    time.sleep(2)

print('-'*20, end='')
print('BOA SORTE!!!', end='')
print('-'*20)

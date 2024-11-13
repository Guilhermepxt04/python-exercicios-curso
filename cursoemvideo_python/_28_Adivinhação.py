import random
from time import sleep

#introdução
print('-' * 32)
print('Bem vindo ao jogo de adivinhação')
print('-' * 32)


#variaveis
numero = list(range(0, 5))
resposta = random.choice(numero)
chute = int(input('chute um numero de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)

#logica
if chute == resposta:
    print('você acertou')
else:
    print('você errou')
    print(f'a resposta era {resposta}')
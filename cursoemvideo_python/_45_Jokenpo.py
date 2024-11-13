from random import choice
from time import sleep
import unidecode

#recursos
cores = {'limpa' : '\033[m', 'verde' : '\033[4;32]', 'vermelho' : '\033[4;31]', 'amarelo' : '\033[33m', 'azul' : '\033[34m'}

#variaveis
c = 0
computador = 0
usuario = 0

#possibilidades de jogadas
jogadas = ['pedra', 'papel', 'tesoura']

#mostrar resultado
def mostrar_resultado(player, boss):
    print(f'{cores["azul"]} {player} X {boss} {cores["limpa"]}')

#verificando vencedor da rodada
def vencedor(player, boss):
    if (player == 'pedra' and boss == 'tesoura') or (player == 'tesoura' and boss == 'papel') or (player == 'papel' and boss == 'pedra'): 
        return 'Você venceu'
    elif player == boss:
        return 'empate'
    else:
        return 'Computador venceu'

#apresentando o jogo
print('='*24)
print('Bem vindo ao JOKENPO!!!')
print('='*24)
print('Ganhe do boss escolhendo entre 3 jogadas [Pedra, Papel, Tesoura]')


#O jogo começou
while c < 3:
    #armazenando e tratando jogadas
    player = input('Faça sua jogada: ').lower().strip()
    player = unidecode.unidecode(player)
    boss = choice(jogadas)

    #verificando se é valida
    if player != jogadas[0] and player != jogadas[1] and player != jogadas[2]:
        print('Por favor escolha uma jogada valida')
        break

    #visual mais bonito
    print(f'{cores["amarelo"]}JO')
    sleep(1)
    print(f'{cores["amarelo"]}KEN')
    sleep(1)
    print(f'{cores["amarelo"]}PO!!!{cores["limpa"]}')

    #logica para ganhar a rodada
    mostrar_resultado(player, boss)
    resultado = vencedor(player, boss)
    print(resultado)
    
    #logica para pontuar
    if resultado == 'Você venceu':
        usuario += 1
    elif resultado == 'Computador venceu':
        computador += 1

    #contador de rodadas
    c += 1

#declarando vencedor
print(f'Você venceu {usuario} rodadas e o computador venceu {computador} rodadas')

if usuario > computador:
    print('Parabéns você venceu')
elif usuario == computador:
    print('Jogo empatado')
else:
    print('Você perdeu ')

print('Fim de jogo')
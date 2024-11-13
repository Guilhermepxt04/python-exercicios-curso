from random import choice #importando biblioteca

win = 0 #declarando variavel

#iniciando o jogo
while True:

    player = str(input('Par ou impar?: ')).strip().lower() #solicitando informação do usuario

    #tratando e validando a informação
    while player != 'par' and player != 'impar': 
        print('Por favor insira uma opção valida')
        player = str(input('Par ou impar?: ')).strip().lower()
    
    #solicitadno variavel do usuario e declarando a da maquina
    n_player = int(input('Escolha um numero de 1 a 10: '))
    n_boss = choice(range(0, 11))
    print(f'O computador jogou {n_boss}')

    #verificando ganhador
    print(f'a soma das escolhas foi {n_player + n_boss},', end='')
    par_impar = (n_player + n_boss) % 2
    if par_impar == 0:
        print('DEU PAR')
        resultado = 'par'
    elif par_impar == 1:
        print('DEU IMPAR')
        resultado = 'impar'

    #computando e somando vitorias / finalizando com a derrota
    if resultado == 'par' and player == "par" or resultado == 'impar' and player == "impar" :
        print('Você ganhou, parabens')
        win += 1
    else:
        print('O computador ganhou, FIM DE JOGO')
        break

#imprimindo quantidade de vitorias
if win == 1:
    print(f'Você ganhou {win} vez, parabens')
elif win == 0:
    print(f'Você não ganhou nenhum vez, tenha mais sorte na proxima')
else:
    print(f'Você ganhou {win} vezes, parabens')

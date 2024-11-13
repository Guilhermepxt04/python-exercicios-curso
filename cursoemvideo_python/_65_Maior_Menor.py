#declarando variaveis
r = 's' #manipulação para iniciar o loop
s = 0 #soma para a media final
c = 0 #contador para a media final

#iniciando loop
while r == 's':
    n = int(input('Digite um numero: ')) #recebendo dados do usuario

    #armezando dados em suas variaveis
    if c == 0:
        maior = n
        menor = n
    if n > maior:
        maior = n
    elif n < menor:
        menor = n

    #aumentando soma e contador de dados para a media
    s += n
    c += 1

    r = str(input('Você quer continuar? [s/n]: ')).strip().lower() #recebendo resposta do usuario
    #tratando variavel r
    while r != 's' and r != 'n':
        print('Por favor insira uma opção valida')
        r = str(input('Você quer continuar? [s/n]: ')).strip().lower()

#informando o usuario dos dados finais
if c == 1:
    print(f'Você digitou {c} valor ')
else:
    print(f'Você digitou {c} valores com a soma entre eles sendo {s}, a média sendo {s / c}. ')

print(f'Maior valor foi {maior} e o menor valor foi {menor}')

cores = {"vermelho" : '\033[31m', 
"amarelo" : '\033[33m', 
"limpa" : '\033[m'}

n = int(input('Digite um numero: '))
cont = 0

for c in range(1, n+1):
    if n % c  == 0:
        print(f'{cores["amarelo"]} {c} {cores["limpa"]} ', end='')
        cont += 1
    else:
        print(f'{cores["vermelho"]} {c} {cores["limpa"]} ', end='')

if cont == 2:
    print(f'O numero {n} é primo pois foi divisível apenas {cont} vezes')
else:
    print(f'O numero {n} não é primo pois foi divisível {cont} vezes')

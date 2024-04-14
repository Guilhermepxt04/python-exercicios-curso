cores = {'limpa' : '\033[m',
'verde' : '\033[4;32m', 
'vermelho' : '\033[4;31',
'azul' : '\033[4;34'}

from random import choice

n = choice(list(range(0, 11)))

print('-'*20)
print('Bem vindo ao jogo ')
print('-'*20)
print(n)

print('Tente acertar o numero em que eu pensei de 0 a 10 ')
resp = int(input(':'))
cont = 1

while resp != n:
    print('Tente acertar o numero em que eu pensei de 0 a 10 ')
    resp = int(input(':'))
    cont += 1

print(f'Parabens você ganhou com {cores["verde"]} {cont} tentativas')

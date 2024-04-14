c = 1
n = 0
c2 = 0
continua = 1

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

print(primeiro_termo)
while c < 11:
    primeiro_termo += razao
    print(primeiro_termo, end='-> ')
    c += 1
    n += 1
print('pausa')

while continua != 0:
    continua = int(input('Quantos termos você quer mostra a mais?: '))
    if continua == 0:
        print(f'p.a finalizada com {n} termos')
    else:
        for c2 in range(0, continua):
            primeiro_termo += razao
            print(primeiro_termo, end='-> ')
            c2 += 1
            n += 1
totc = 0
totn = 0
resp = 's'

while resp == 's':
    nome = str(input('Digite seu nome: ')).strip().lower()
    if nome[0] == 'c':
        totc += 1
    else:
        totn += 1
    resp = str(input('Quer digitar mais nomes? [S / N]: '))




print(f'ao todo foram {totn} nomes informados, mas apenas {totc} começam com a letra C ')

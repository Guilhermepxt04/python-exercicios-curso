n0 = int(input('Digite o 1. valor: '))
n1 = int(input('Digite o 2. valor: '))
n2 = int(input('Digite o 3. valor: '))
n3 = int(input('Digite o 4. valor: '))

tabela = (n0, n1, n2, n3)

print(f'o numero 9 apareceu {tabela.count(9)} vezes')

if 3 in tabela:
    print(f'o numero 3 apareceu na posição {tabela.index(3) + 1}')

print('os numeros pares digitados foram: ', end='')
for c in range(len(tabela)):
    par = tabela[c] % 2
    if par == 0:
        print(f'{tabela[c]}', end=' ' )

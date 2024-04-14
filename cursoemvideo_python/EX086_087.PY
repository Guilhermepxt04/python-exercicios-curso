matriz = [[], [], []]

soma_par = 0
soma_coluna3 = 0
maior_valor_linha2 = 0

for x in range(3):
        for y in range(3):

            valor = int(input(f'Digite um valor para a posição [{x};{y}]: '))
            if valor % 2 == 0:
                soma_par += valor

            if y == 2:
                soma_coluna3 += valor

            matriz[x].append(valor)

            if x == 1:
                if valor > maior_valor_linha2:
                    maior_valor_linha2 = valor

for l in range(3):
    print()
    for n in (matriz[l]):
        print(f'[{n:^5}]', end='')

print()

print(f'A soma dos valores pares foi {soma_par}')
print(f'A soma dos valores da terceira coluna foi {soma_coluna3}')
print(f'O maior valor da 2 linha foi {maior_valor_linha2}')

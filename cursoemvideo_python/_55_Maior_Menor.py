maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'digite o peso da {c} pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior :
        maior = peso
    if peso < menor:
        menor = peso

print(f'O maior peso lido foi {maior}')
print(f'O menor peso lido foi {menor}')

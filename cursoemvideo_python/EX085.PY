numeros = [[], []]

for c in range(0, 7):
    n = int(input(f'Digite o {c + 1} valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
        numeros[0].sort()
    else:
        numeros[1].append(n)
        numeros[1].sort()

print(f'os numeros impares em ordem crescente são: {numeros[1]}')
print(f'os numeros pares em ordem crescente são: {numeros[0]}')

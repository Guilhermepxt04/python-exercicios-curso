s = 0
i = 0

for c in range(0, 500, 3):
    if c % 2 == 1:
        s += c
        i += 1
print(f'A soma dos {i} impares multiplos de 3 é igual a {s}')

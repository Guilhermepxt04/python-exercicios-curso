num = []


while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    print(f'valor {n} foi adicionado a lista')
    num.sort(reverse=True)

    resp = str(input('Quer adicionar mais um valor?: [S/N]')).lower().strip()
    if resp == 'n':
        break
    while resp != 's' and resp != 'n':
        print('Por favor insira uma opção valida')
        resp = str(input('Quer adicionar mais um valor?: [S/N]')).lower().strip()

print(f'Voce digitou {len(num)} valores')

print(f'A lista em ordem decrescente fica', end=' ')
print(num)

if 5 in num:
    print('O valor 5 está na lista nas posições: ', end=' ')
for i, n in enumerate(num):
    if n == 5:
        print(i, end=' ')
else:
    print('O valor 5 não está na lista')
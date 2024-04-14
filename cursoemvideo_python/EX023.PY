n = str(input('digite um numero de até 4 digitos: ')).strip()

if len(n) == 4:
    print(f'milhar {n[0]}')
    print(f'centena {n[1]}')
    print(f'dezena {n[2]}')
    print(f'unidade {n[3]}')
elif len(n) == 3:
    print(f'centena {n[0]}')
    print(f'dezena {n[1]}')
    print(f'unidade {n[2]}')
elif len(n) == 2:
    print(f'dezena {n[0]}')
    print(f'unidade {n[1]}')
elif len(n) == 1:
    print(f'unidade {n[0]}')
else: len(n) > 4
print('o programa só aceita numeros de até 4 algarismos e sem espaços entre eles')
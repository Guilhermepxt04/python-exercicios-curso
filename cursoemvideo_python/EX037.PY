number = int(input('Digite um valor: '))

print('=' *10, end='')
print('MENU DE CONVERSÃO', end='')
print('=' *10)

print('''Escolha sua conversão:
[1] Binario
[2] Hexadecimal
[3] Octal''')
conversor = int(input(': '))

if conversor == 1:
    print(f'O numero {number} convertido para binario fica {number:b}')
elif conversor == 2:
    print(f'O numero {number} convertido para hexadecimal fica {number:x}')
elif conversor == 3:
    print(f'O numero {number} convertido para octal fica {number:o}')
else:
    print('Por favor insira uma forma valida')
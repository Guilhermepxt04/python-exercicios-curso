sexo = str(input('Digite seu sexo biologico [M/F]:  ')).upper().strip()

while sexo != 'M' and sexo != 'F':
    print('Por favor insira uma opção valida: [M/F]')
    sexo = str(input('Digite seu sexo biologico [M/F]:  ')).upper().strip()

if sexo == 'M':
    print('Seu sexo biologico é masculino')
else:
    print('Seu sexo biologico é feminino')

while True:
    if resp == 'n':
        break

    saque = int(input('Quanto você quer sacar: '))
    valor = saque

    notas_50 = int(saque / 50)
    saque -= 50 * notas_50

    notas_20 = int(saque / 20)
    saque -= 20 * notas_20

    notas_10 = int(saque / 10)
    saque -= 10 * notas_10

    notas_01 = int(saque / 1)

    print(f'O saque em um valor de R${valor:.2f} foi feito da seguinte forma: ')
    if notas_50 > 0:
        print(f' {notas_50} notas de 50 reais')
    if notas_20 > 0:
        print(f' {notas_20} notas de 20 reais')
    if notas_10 > 0:
        print(f' {notas_10} notas de 10 reais')
    if notas_01 > 0:
        print(f' {notas_01} moedas de 1 real')

    resp = str(input('Quer sacar mais?[S/N]: ')).lower().strip()

print('Fim do programa, volte sempre :)')

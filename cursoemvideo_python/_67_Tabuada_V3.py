while True:
    print('-'*20)
    n = int(input('Digite um numero para ver sua tabuada (negativo para fechar o programa): '))
    if n < 0:
        print('Programa encerrado')
        break
    for c in range(1,11):
        x = n * c
        print(f'{n} x {c} = {x}')

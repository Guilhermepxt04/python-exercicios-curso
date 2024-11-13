extensos = ('zero', 'um', 'dois' , 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input(('Qual numero você quer ler por extenso? [0 a 20]: ')))
    while n != len(extensos) - 1 :
        print('tente novamente')
        n = int(input(('Qual numero você quer ler por extenso? [0 a 20]: ')))

    escrito = str(extensos[n])

    print(f'O numero {n} escrito por extenso fica {escrito.upper()}')


n = int(input('digite um numero: '))

def par_impar(n):
    if n % 2 == 1:
        print(f'o numero {n} é impar')
    else:
        print(f'o numero {n} é par')
        return n

par_impar(n)
print('fim do programa')


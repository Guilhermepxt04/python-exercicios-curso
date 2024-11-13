x = int(input('digite um numero: '))
contador = 1

print(f'a tabuada do numero {x} é')
print('-'*12)
while (contador <= 10):
    r = x * contador
    print(f'{x} x {contador} = {r}  ')
    contador = contador + 1
print('-'*12)

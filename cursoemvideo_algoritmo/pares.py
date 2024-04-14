total_par = 0
total_impar = 0
resp = "s"

def par (n):
    if n % 2 == 1:
        print('impar')
    else:
        print('par')
    return(n)

while resp == "s":
    n = int(input('Digite um valor: '))
    n = par(n)
    if n % 2 == 1:
        total_impar += 1
    else:
        total_par += 1
    resp = str(input('Quer continuar?[S / N]: ')).lower()

print(f'houve um total de {total_par} valores pares, e {total_impar} de valores impares')
print('fim do programa')
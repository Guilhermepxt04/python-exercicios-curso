D = int(input('quantos dias o carro ficou alugado? '))
KM = float(input('quantos KM rodou?'))
preço = (D * 60) + (0.15 * KM)
print(f'o preço total a pagar é de {preço:.2f}R$')
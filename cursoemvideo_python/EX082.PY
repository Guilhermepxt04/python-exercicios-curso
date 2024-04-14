num = list()
par = list()
impar = list()


while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer adicionar outro valor?: [S/N] ')).lower().strip()
    if resp == 'n':
        break
    while resp != 's' and resp != 'n':
        print('Por favor insira uma opção valida')
        resp = str(input('Quer adicionar outro valor?: [S/N] ')).lower().strip()

for n in (num):
    if n % 2 == 0:
        par.append(num[num.index(n)])
    else:
        impar.append(num[num.index(n)])

print(num)
print(par)
print(impar)
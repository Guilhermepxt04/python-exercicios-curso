#recursos
cores = { 'limpa' : '\033[m',
'verde' : '\033[4;32m',
'vermelho' : '\033[4;32m',
'amarelo' : '\033[4;32m' ,}

#variavies
a = float(input('Primeiro segmento: '))
b = float(input('Primeiro segmento: '))
c = float(input('Primeiro segmento: '))

#lógica
analise = b - c < a < b + c and a - c < b < a + c and a - b < c < a + b

#condição para criar o triangulo
if analise == True :
    print('os segmentos podem formar um ', end='')
else:
    print('os segmentos não podem formar um triangulo')

#condição para classificar o triangulo
if analise == True:
    if a == b == c:
        print(f'{cores["verde"]}Triangulo Equilatero')
    elif a == b != c or a == c != b or b == c != a:
        print(f'{cores["vermelho"]}Triangulo Isosceles')
    elif a != b and a != c and b != c:
        print(f'{cores["amarelo"]}Triangulo escaleno')
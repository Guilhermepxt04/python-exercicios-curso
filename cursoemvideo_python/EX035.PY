#variavies
a = float(input('Primeiro segmento: '))
b = float(input('Primeiro segmento: '))
c = float(input('Primeiro segmento: '))

#lógica
analise = b - c < a < b + c and a - c < b < a + c and a - b < c < a + b

#condição
if analise == True :
    print('os segmentos podem formar um triangulo')
else:
    print('os segmentos não podem formar um triangulo')
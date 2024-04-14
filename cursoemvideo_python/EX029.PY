#variaveis
velocidade = int(input('digite a velocidade do carro: '))
multa = (velocidade-80)*7

#logica
if velocidade > 80:
    print(f'você ultrapassou o limite de velocidade e será multado em R${multa:.2f} ')
else:
    print('dentro do limte de velocidade parabéns!!! Tenha uma otima semana')
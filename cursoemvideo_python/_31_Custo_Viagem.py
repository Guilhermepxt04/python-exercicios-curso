distancia = int(input("digite a distancia da viagem: "))

print(f'Você irá fazer uma viagem de {distancia}KM')
if distancia > 200:
    preço = (0.45*distancia)
    print(f'o preço da sua passagem será de {preço:.2f} reias')
else:
    preço = (0.50*distancia)
    print(f'o preço da sua passagem será de {preço:.2f} reias')
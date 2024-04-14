import math

cat_oposto = float(input("comprimento do cateto oposto: ")) 
cat_adjacente = float(input('comprimento do cateto adjacente: ')) 
hipo = math.hypot(cat_oposto, cat_adjacente)
print(f'o valor da sua hipotenusa é de {hipo:.4f}')
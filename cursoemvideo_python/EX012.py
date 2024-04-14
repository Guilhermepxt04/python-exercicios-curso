#VO = float(input('digite o valor original do produto: '))
#desc = float(input('digite a porcentagem de desconto: '))
#descapl = desc / 100
#VPD = VO * descapl
#VA = VO - VPD
#print(f'o valor original de {VO} na promoção com {desc}% de desconto caiu para {VA}!!!')

preço = float(input('digite o valor de um produto: '))
desc = float(input('digite a porcentagem de desconto: '))
novo = preço - (preço * desc / 100)
print(f'o valor do produto era de {preço:.2f} mas com o desconto de {desc:.2f}% agora está custando {novo:.2f}!!!') 
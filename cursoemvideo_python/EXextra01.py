cores = {'limpa' : '\033[m',
'verde' : '\033[4;32m',
'vermelho' : '\033[4;31m'}



preco = float(input('digite o valor de um produto: '))
descvista = float(input('digite uma porcentagem de desconto para pagamento a vista: '))
vista = preco - (preco / 100 * descvista)
juros = float(input('digite uma porcentagem para juros para pagamento parcelado? '))
parcelado = preco + (preco / 100 * juros)
print(f'o valor original do produto é de {preco:.2f} com pagamento a vista cai para {cores["verde"]}{vista:.2f}{cores["limpa"]} com {cores["verde"]}{descvista}{cores["limpa"]}', end="")
print(f'% de desconto, parcelado o preço sobe para {cores["vermelho"]}{parcelado:.2f}{cores["limpa"]} com {cores["vermelho"]}{juros}{cores["limpa"]}% de juros')
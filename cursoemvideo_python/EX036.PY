#Cores 
cores = {'limpa' : '\033[m','verde' : '\033[4;32m','vermelho' : '\033[4;31m','amarelo' : '\033[4;33m','azul' : '\033[4;34m'}

#Declarando variaveis 
house = float(input('Qual o valor da casa?: '))
wage = float(input('Qual o seu salário mensal?: '))
years = int(input('Quantos anos pretende pagar?: '))
portion = house / (years * 12)

#Logica para emprestimo
print(f'Para pagar uma casa de {cores["azul"]}R${house:.2f}{cores["limpa"]} em {years} anos, o valor da parcela será de {cores["amarelo"]}R${portion:.2f}{cores["limpa"]}')
if portion > wage / 100 * 30:
    print(f'{cores["vermelho"]}Emprestimo negado{cores["limpa"]}')
else:
    print(f'{cores["verde"]}Emprestimo aprovado{cores["limpa"]}')
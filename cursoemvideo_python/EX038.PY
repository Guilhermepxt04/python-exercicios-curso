#cores
cores = {'limpa' : '\033[m',
'verde' : '\033[4;32m', 
'vermelho' : '\033[4;31'}

#variaveis
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um segundo valor: '))

if n1 > n2:
    print(f'O valor {cores["verde"]}{n1}{cores["limpa"]} (primeiro valor digitado) é o maior')
elif n2 > n1:
    print(f'O valor {cores["verde"]}{n2}{cores["limpa"]}(segundo valor digitado) é o maior')
elif n1 == n2:
    print(f'Não existe valor {cores["vermelho"]}mmaior{cores["limpa"]}, os dois são iguais')
#declarando lista e variavel para iniciar o programa 
num = list()


#iniciando o laço
while True:
    n = int(input('Digite um valor: ')) #solicitando informação para o usuario

    if n not in num: #verificando se o numero esta na lista
        num.append(n) #adicionando numero caso não esteja
        print('Valor adicionado a lista')

    else: #recusando adição caso duplicado
        print('Valor duplicado, não adicionado a lista')

    resp = str(input('Quer informar mais um numero?: [S/N]')).strip().lower() #verificando se o usuario ira continuar ou nao
    if resp == 'n':
        break

    while resp != 's' and  resp != 'n': #tratando e validando info dada pelo usuario
        print('Por favor insira uma opção valida:')
        resp = str(input('Quer informar mais um numero?: [S/N]')).strip().lower()

num.sort() #ordenado a lista em ordem crescente
print(f'os valores digitados foram {num}') #imprimindo a lista

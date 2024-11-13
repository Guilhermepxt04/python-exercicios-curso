#declarando a lista
num = list()

#pedindo informações para o usuario inserir na lista
for n in range(0,5):
    num.append(int(input('Digite um valor: ')))
    print(num)

#imprimindo qual foi o maior valor
print(f'O maior valor foi {max(num)} nas posições:', end=' ')

#iniciando o laço para ler os valores e seus index na lista
for i, n in enumerate(num):
    if n == max(num): #imprimindo o index do numero caso ele seja o maior 
        print(i, end=' ')

#imprimindo qual foi o menor valor
print(f'\nO menor valor foi {min(num)} nas posições:', end=' ')

#iniciando o laço para ler os valores e seus index na lista
for i, n in enumerate(num):
    if n == min(num): #imprimindo o index do numero caso ele seja o menor 
        print(i, end=' ')

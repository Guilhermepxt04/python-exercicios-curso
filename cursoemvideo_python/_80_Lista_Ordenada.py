num = list() #declarando a lista

#iniciando o laço de adição de valores
for c in range(0, 5):
    #adicionando o primerio valor
    if c == 0:
        num.append(int(input(f'Digite o {c} valor: ')))
        print('Numero adicionado no final da lista')

    #adicionando e já ordenando valores seguintes
    else:
        valor = int(input(f'Digite o {c} valor: '))

        for n in (num): #verificando index e numero de cada valor já na lista 
            #colocando o valor assim que encontrar um n maior que ele
            if valor < n:
                num.insert(num.index(n), valor)
                print(num.index(valor))
                break

            #colocando o valor no final da lista se ele for maior que o numero maximo da lista
            elif valor > max(num):
                num.append(valor)
                print('Numero adicionado no final da lista')
                break
print(num)
#declarando listas e variaveis
clientes = list()
dados = list()
total_clientes = 0
peso = 0

cadastros = int(input('Quantos usuarios serão cadastrados?: ')) #solicitando quantos cadastros serão feitos

#iniciando loop de cadastros
for c in range(cadastros):
    #solicitando dados e armazenando nas listas
    dados.append(str(input('Digite o nome do cliente: ')))
    peso = float(input('Digite o peso do cliente: '))
    dados.append(peso)
    clientes.append(dados[:])
    dados.clear() #limpando dados para adicionar outro cliente

    #registrando o maior e menor peso cadastrado
    if c == 0:
        maior_peso = menor_peso = peso

    if peso > maior_peso:
        maior_peso = peso
    elif peso < menor_peso:
        menor_peso = peso


    total_clientes += 1 #somando o total de clientes

    #verificações para interromper ou não o loop
    if c == cadastros - 1:
        break
    resp = str(input('Quer continuar?: ')).lower()
    if resp == 'n':
        break

#imprimindo todos os clientes cadastrados 
print(f'Ao todo você cadastrou {total_clientes} clientes')

#imprimindo os mais pesados
print(f'Os clientes mais pesados cadastrados estão com {maior_peso:.2f}KG e são respectivamente:', end=' ')
for u in (clientes):
    for d in u:
        if d == maior_peso :
            print(u[0], end=' , ')

print('\n')

#imprimindo os mais leves
print(f'Os clientes mais leves cadastrados estão com {menor_peso:.2f}KG e são respectivamente:', end=' ')
for u in (clientes):
    for d in u:
        if d == menor_peso :
            print(u[0], end=' ')

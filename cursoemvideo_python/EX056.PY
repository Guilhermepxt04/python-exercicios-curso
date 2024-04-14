#declarando variaveis
idade_media = 0
mulher_20 = 0
velho_idade = 0

analise = int(input('Quantas pessoas serão analisadas?: '))

#começando analise de pessoas
for p in range(1, analise + 1):
    print(f'----- {p} PESSOA -----') #contador de pessoas
    nome = str(input('Nome: ')).strip().capitalize() #recebendo e tratando nome

    idade = int(input('Idade: ')) #recebendo idade
    idade_media += idade #somando para media final

    sexo = str(input('Sexo: [M/F]: ')).strip().upper() #recebendo e tratando sexo
    if sexo != 'F' and sexo != 'M': #verificando se o sexo é valido
        print('Por favor insira um sexo valido')
        break

    if sexo == 'F' and idade < 20: #contador para mulheres com menos de 20 anos
        mulher_20 += 1

    if idade > velho_idade and sexo == 'M': #analise para o homem mais velho analisado
        velho_idade = idade
        velho_nome = nome

print(f'a média de idade das pessoas analisada é {idade_media/4}')

if mulher_20 == 1:
    print(f'{mulher_20} mulher com menos de 20 anos foi analisada')
else:
    print(f'{mulher_20} mulheres com menos de 20 anos foram analisadas')

print(f'O homem mais velho se chama {velho_nome} e tem {velho_idade}')
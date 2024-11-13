#declarando variaveis para armazenar dados solicitados
maior_18 = 0
homens = 0
mulher_sub20 = 0
cadastrar = ''

#iniciando o programa
while True:

    #verificando se o loop continua
    if cadastrar == 'n':
        print('Fim dos cadatros')
        break

    #começando o loop
    else:
        #solicitando e tratando o sexo fornecido pelo usuario
        sexo = ''
        while sexo != 'm' and sexo != 'f':
            sexo = str(input('Qual o sexo da pessoa cadastrada?[M/F]: ')).lower().strip() [0]

        idade = int(input('Quantos anos essa pessoa tem?: ')) #solicitando idade

        #adicionando quantidades de dados especificos
        if sexo == 'm':
            homens += 1
        if idade > 18:
            maior_18 += 1
        if sexo == 'f' and idade < 20:
            mulher_sub20 += 1
        
        cadastrar = str(input("Quer continua?[S/N]: ")).lower().strip() #interação para continuar o loop

#imprimindo todas as info solicitadas após os cadastros 
if maior_18 == 1:
    print(f'{maior_18} pessoa maior que 18 anos  foi cadastrada ')
else:
    print(f'{maior_18} Pessoas maiores de 18 anos foram cadastradas')

if homens == 1:
    print(f'{homens} homem foi cadastrado ')
else:
    print(f'{homens} Homens foram cadastrados')

if mulher_sub20 == 1:
    print(f'{mulher_sub20} mulher com menos de 20 anos foi cadastrada ')
else:
    print(f'{mulher_sub20} Mulheres com menos de 20 anos foram cadastradas')

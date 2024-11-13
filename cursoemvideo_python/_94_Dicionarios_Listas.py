dados = dict()
pessoas = list()
mulheres = list()
acima_da_media = list()

mulher = False
maior_que_media = False

while True:
    nome = str(input("Qual seu nome?: ")).strip()
    sexo = str(input("Qual seu sexo?[M/F]: ")).lower().strip()
    while sexo != 'm' and sexo != 'f':
        print('digite uma opção valida[M/F]:  ')
        sexo = str(input("Qual seu sexo?[M/F]: ")).lower().strip()
    idade = int(input("Qual sua idade?: "))

    dados = {
        'nome': nome,
        'sexo': sexo,
        'idade': idade
    }

    pessoas.append(dados)

    continuar = str(input("Quer cadastrar mais uma pessoa:? [S/N]")).lower().strip()
    while continuar != 's' and continuar != 'n':
        print('Digite uma opção valida[S/N]: ')
        continuar = str(input("Quer cadastrar mais uma pessoa?: ")).lower().strip()
    if continuar == 'n':
        break


idade = 0

print(f"{len(pessoas)} pessoas foram cadastradas")

for i, v in enumerate(pessoas):
    idade += pessoas[i]['idade']

    if pessoas[i]['sexo'] == 'f':
        mulheres.append(pessoas[i]['nome'])
        mulher = True

idade_media = float(idade / len(pessoas))

for i, v in enumerate(pessoas):
    if pessoas[i]['idade'] > idade_media:
        acima_da_media.append(pessoas[i])
        maior_que_media = True

print(f'a média de idade é {idade_media:.2f}')

print('-=' * 30)

if mulher == True:
    print(f'as mulheres cadastradas foram {mulheres}')

print('-=' * 30)

if maior_que_media == True:
    print(f'essas pessoas estão acima da idade media {acima_da_media}')

pessoas = list()
dados = list()

for d in range(0,3):
    dados.append(str(input('Digite o nome do usuario: ')))
    dados.append(int(input('Digite a idade do usuario: ')))
    pessoas.append(dados[:])
    dados.clear()

print(pessoas)

for c in pessoas:
    for d in c:
        print('BATATA')
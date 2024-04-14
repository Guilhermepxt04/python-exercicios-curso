geral = list()
alunos = list()
notas = list()
soma = 0

while True:
    alunos.append(str(input('Digite um nome: ')))
    notas.append(int(input('Digite a nota do aluno: ')))
    notas.append(int(input('Digite a nota do aluno: ')))
    alunos.append(notas[:])
    geral.append(alunos[:])
    alunos.clear()
    notas.clear()
    
    r = str(input('Quer cadastrar mais um aluno?[S/N]: ')).strip().lower()
    if r == 'n':
        break

print(geral)

for g in range(len(geral)):
    n = geral[g][1]
    print(n)
    media = (n[0] + n[1]) / 2
    print(f'{media:.2f}')

pesquisa = str(input('Quer ver as notas de qual aluno?: ')).lower().strip()

for g in range(len(geral)):
    if pesquisa in geral[g]:
        print(geral[g])
geral = list()
alunos = list()
notas = list()

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

print(f'{'Nº':<10} {'Nome':<10} {'media':<10}')
print('='*40)
for g in range(len(geral)):
    n = geral[g][1]
    media = (n[0] + n[1]) / 2
    print(f'{g:<10} {geral[g][0]:<10} {media:<10.2f}')

print('='*40)
while True:
    pesquisa = str(input('Quer ver as notas de qual aluno?[999 interrompe]: ')).lower().strip()
    if pesquisa == '999':
        break
    for g in range(len(geral)):
        if pesquisa in geral[g]:
            print(geral[g][0], end=' ')
            print(geral[g][1])     

print('Fim do programa')   
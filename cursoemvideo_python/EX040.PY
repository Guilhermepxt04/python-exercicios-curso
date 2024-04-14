import time

#cores
cores = {'limpa' : '\033[m', 
'verde' : '\033[4;32m', 
'vermelho' : '\033[4;31m]',
'azul' : '\033[4;34m'}

#variaveis
n1 = float(input('digite a primeira nota do aluno: '))
n2 = float(input('digite a segunda nota do aluno: '))
m = (n1 + n2) / 2
print(f'A média do aluno foi de {m:.2f}, o aluno está:')
print('...')
time.sleep(3)

#logica para aprovação
if m >= 7:
    print(f'{cores["verde"]}O aluno está aprovado')
elif 5 < m < 6.9:
    print(f'{cores["azul"]}O aluno está de recuperação')
else:
    print(f'{cores["vermelho"]} O aluno está reprovado')
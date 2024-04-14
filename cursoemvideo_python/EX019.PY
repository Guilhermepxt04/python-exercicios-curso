import random

A1 = input('nome do primeiro aluno: ')
A2 = input('nome do segundo aluno: ')
A3 = input('nome do terceiro aluno: ')
A4 = input('nome do quarto aluno: ')
sorteio = [A1, A2, A3, A4]
R = random.choice(sorteio)
print(f'o aluno sorteado foi {R}')
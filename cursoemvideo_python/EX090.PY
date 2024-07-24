nome = str(input('Qual o nome do aluno?: ')).strip().capitalize()
nota_1 = float(input('Qual a primeira nota do aluno?: '))
nota_2 = float(input('Qual a segunda nota do aluno?: '))

media = (nota_1 + nota_2) / 2

if media > 7:
    situação = str('aprovado')
elif 5 < media < 7:
    situação = str('recuperação')
else:
    situação = str('reprovado')

aluno={'Nome': f'{nome}',
        'Media': f'{media}',
        'Situação': f'{situação}'
        }

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

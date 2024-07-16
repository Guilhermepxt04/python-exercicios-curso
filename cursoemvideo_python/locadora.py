filmes = dict
locadora = []

while True:
    titulo = str(input('Digite o titulo do filme: '))
    ano = int(input('digite o ano de lançamento do filme: '))
    genero = str(input('digite o genero do filme: '))
    filmes={'titulo': f'{titulo}',
            'ano': f'{ano}',
            'genero': f'{genero}'
            }
    locadora.append(filmes)
    r = str(input('tem mais filmes para adicionar?[S/N]:')).strip().lower()
    if r == 'n':
        break

print(filmes.items())

for k, v in filmes.items():
    print(f'o {k} é {v}') 


print(locadora)

i = int(input('qual filme vc quer ver?: '))

print(locadora[i])
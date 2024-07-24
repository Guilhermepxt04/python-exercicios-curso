filmes = dict
locadora = list()

while True:
    titulo = str(input('Digite o titulo do filme: '))
    ano = int(input('digite o ano de lançamento do filme: '))
    genero = str(input('digite o genero do filme: '))
    filmes={'titulo': titulo,
            'ano': ano,
            'genero': genero
            }
    locadora.append(filmes)
    r = str(input('tem mais filmes para adicionar?[S/N]:')).strip().lower()
    if r == 'n':
        break

print(filmes.items())

for k, v in filmes.items():
    print(f'o {k} é {v}') 


print(locadora)

for k,v in enumerate(locadora):
    print(locadora[k]['titulo'])
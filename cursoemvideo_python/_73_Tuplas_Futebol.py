tabela = ('palmeiras', 'gremio', 'atletico mg', 'flamengo', 'botafogo', 'bragantino', 'fluminense', 'athletico pr', 'internacional', 'fortaleza', 'sao paulo', 'cuiaba', 'corinthians', 'cruzeiro', 'vasco da gama', 'bahia', 'santos', 'goias', 'coritiba', 'america mg')
sorted_tabela = sorted(tabela)
pesquisa = ''

print('Tabela do brasileirão')
print('-'*100)
print(tabela)
print('-'*100)

print(f'Os 5 primeiros colocados são: {tabela[0:5]},')
print('-'*60)

print(f'os 4 ultimos colocados são: {tabela[16:20]} ')
print('-'*60)

print(f'a tabela em ordem alfabetica fica')
print(sorted_tabela)
print('-'*60)

while pesquisa not in tabela:
    pesquisa = str(input('qual time você quer ver a posição?: ')).lower()

print(f'o time {pesquisa} está na posição {tabela.index(pesquisa) + 1}')

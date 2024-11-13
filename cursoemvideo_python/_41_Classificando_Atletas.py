from datetime import date

#recursos
cores = { 'limpa' : '\033[m',
'verde' : '\033[4;32m',
'vermelho' : '\033[4;32m'}

#variaveis
year = int(input('Digite a idade do atleta: '))
age = date.today().year - year

#validando informação
if year > date.today().year:
    print(f'Por favor insira um ano valido (Anos anteriores a {date.today().year} )')


#logica da categoria
if year < date.today().year:
    print(f'O atleta tem {age} anos')
    if age <= 9:
        print('Categoria: Mirim')
    elif 10 <= age <= 14:
        print('Categoria: infantil')
    elif 15 <= age <= 19:
        print('Categoria: junior')
    elif age == 20:
        print('Categoria: senior')
    elif age > 20:
        print('Categoria: master')
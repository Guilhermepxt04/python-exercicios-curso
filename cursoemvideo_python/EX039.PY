from datetime import date

#cores
cores = {'limpa' : '\033[m',
'verde' : '\033[4;32m', 
'vermelho' : '\033[4;31',
'azul' : '\033[4;34'}

#variaveis
year = int(input('digite seu ano de nascimento: '))
age = date.today().year - year
wait = 18 - age
delay = age - 18

#verificando informação do usuario
if year > date.today().year:
    print(f'Por favor insira um ano valido (Anos anteriores a {date.today().year})')

#logica para o alistamento
if year <= date.today().year:
    print(f'Você nasceu em {year} e tem {age} anos')

    if age < 18:
        print(f'Você ainda precisa esperar mais {cores["verde"]}{wait} anos para se alistar no exercito')

    elif age == 18:
        print(f'{cores["verde"]}Você tem que se alistar IMEDIATAMENTE!!!')

    elif age > 18 and delay == 1:
        print(f'Passou da hora de alistar no exercito, você está com um atraso de {cores["vermelho"]}m{delay} {cores["limpa"]} ano')
        print(f'Seu alistamento deveria ter sido em {date.today().year - 1}')

    else:
        print(f'Passou da hora de alistar no exercito, você está com um atraso de {cores["vermelho"]}m{delay} {cores["limpa"]} anos')
        print(f'Seu alistamento deveria ter sido em {date.today().year - delay}')
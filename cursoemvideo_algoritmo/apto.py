from datetime import date

print('-'*25)
print('DEPARTAMENTO DE TRANSITO')
print('-'*25)

ano_atual = date.today().year
ano_nascimento = int(input('Em que ano você nasceu?: '))
verificando = ano_atual - ano_nascimento
espera = 18 - verificando

print ('-'*12, end='')
print ('STATUS', end='')
print ('-'*12)

if verificando > 18:
    print('Você pode dirigir')
else:
    print('você não pode dirigir')
    print(f'espere por mais {espera} anos')
print('-'*30)

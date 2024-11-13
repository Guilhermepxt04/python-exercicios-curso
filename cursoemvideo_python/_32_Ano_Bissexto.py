from datetime import date

#verificando ano 
ano = int(input('digite um ano para analisar (digite 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
#verificando condições para bissexto
mult400 = ano % 400
mult4 = ano % 4
lista = range(100, 9001, 100)
#logica
if ano in lista:
    print('ano não bissexto')
elif mult4 == 0 & mult400 == 0:
    print('ano bissexto')
else:
    print('ano não bissexto')
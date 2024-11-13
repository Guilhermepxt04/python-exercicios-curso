expressao = input('Digite uma expressao matematica: ')
expressao_lista = list(expressao)

par_aberto = 0
par_fechado = 0

for c in expressao_lista:
    if c == '(':
        par_aberto += 1
    elif c == ')':
        par_fechado += 1

if par_aberto == par_fechado:
    print('Expressão valida')
else:
    print('Expressão invalida')
    
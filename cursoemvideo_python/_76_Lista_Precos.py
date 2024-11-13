tabela = ('lapis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo', 25.00, 'mochila', 120.32)

print('-'*20)
print('TABELA DE PREÇOS')
print('-'*20)

for c in range(0, len(tabela)):

    if type(tabela[c]) == str:
        print(f'{tabela[c]:.<15}', end='')

    elif type(tabela[c]) == float:
        print(f'R$ {tabela[c]:.2f}')

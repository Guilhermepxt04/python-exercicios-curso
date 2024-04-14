#import re

tabela = ('hamburguer', 'suco', 'batata', 'pizza')

#for c in range(len(tabela)):
    #palavra_vogal = re.sub(r'[^aeiouAEIOU]', ' ', tabela[c])
    #print(f'As vogais das palavras {tabela[c]:<10} são: ', end=' ')
    #print(f'{palavra_vogal:<10}')

for p in tabela:
    print(f'\n na palavra {p} temos as vogais:  ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
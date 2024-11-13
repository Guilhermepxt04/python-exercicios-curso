from datetime import date

nome = str(input('Digite um nome: '))
nascimento = int(input('Digite o ano de nascimento: '))
carteira_de_trabalho = int(input('Digite o CTPS: '))
idade = date.today().year - nascimento

if carteira_de_trabalho != 0:

    ano_de_contratação = int(input('Digite o ano de contratação: '))
    salario = float(input('digite o salário:'))
    contribuição = date.today().year - ano_de_contratação
    if contribuição >= 35:
        aposentadoria = 'aposentado'
    else: 
        aposentadoria = f'ainda faltam {35-contribuição} anos para aposentadoria, irá se aposentar com {idade + (35-contribuição) }'

    pessoa = {'Nome': nome,
            'Idade': idade,
            'CTPS': carteira_de_trabalho,
            'Contratação': ano_de_contratação,
            'Salário': salario,
            'Aposentadoria': aposentadoria}
    
    for k, v in pessoa.items():
        print(f'{k}: {v}')

else:
    pessoa = {'Nome': nome,
            'Idade': idade,
            'CTPS': carteira_de_trabalho}
    
    for k, v in pessoa.items():
        print(f'{k}: {v}')

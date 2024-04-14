#declarando variaveis
soma_total = 0
maior_1000 = 0
c = 0
barato = 0
resp = 's'

#iniciando cadastro de produtos
while True:
    if resp == 'n': #verificando se os cadastros devem continuar
        break

    #pedindo informações para o usuario
    nome_produto = str(input('Nome do produto: ')).capitalize().strip()
    preço = float(input('Valor do produto R$: '))

    #salvando a variavel do produto mais barato com seu nome e valor
    if c == 0 or preço < barato:
        barato = preço
        nome_barato = nome_produto

    #soma total da compra
    soma_total += preço

    #produtos maiores que mil reias
    if preço > 1000:
        maior_1000 += 1

    #contador de produtos cadastrados
    c += 1

    #verificando se os cadastros devem continuar
    resp = str(input('Quer continuar?[S/N]: ')).lower().strip()
    while resp != 's' and resp != 'n':
        resp = str(input('Quer continuar?[S/N]: ')).lower().strip()

#imprimindo informações da compra
print(f'O total da compra foi R${soma_total:.2f} cadastrando {c} produtos')
print(f'Temos {maior_1000} produtos custando mais que R$1000 reais')
print(f'O produto mais barato foi {nome_barato} custando R${barato:.2f}')

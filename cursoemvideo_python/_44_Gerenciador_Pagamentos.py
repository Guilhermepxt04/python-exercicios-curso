#recursos
colors = { 'limpa' : '\033[m',
'verde' : '\033[4;32m',
'vermelho' : '\033[4;31m',
'amarelo' : '\033[4;33m' ,}

#variaveis
value = float(input('Digite o valor original do produto: '))

#metodos de pagamento
print('Selecione o metodo de pagamento: ')
print('[1] Para dinheiro/cheque')
print('[2] A vista no cartão')
print('[3] Em até 2x no cartão')
print('[4] 3x ou mais no cartão')
payment = int(input(':'))

#logica para pagamentos
if payment == 1:
    value = value - (value / 100 * 10)
    print(f'O valor total a pagar será de {value:.2f} com 10% de desconto')
elif payment == 2:
    value = value - (value / 100 * 5)
    print(f'O valor total a pagar será de {value:.2f} com 5% de desconto')
elif payment == 3:
    value = value / 2
    print(f'O preço por parcela do produto será de {value:.2f}')
elif payment == 4:
    installments = int(input('Digite a quantidade de parcelas: '))
    valuet = value + (value / 100 * 5 * installments)
    value = valuet / installments
    print(f'O preço por parcela do produto será de {value:.2f} e seu preço total será de {valuet} ')
else:
    print('Por favor, insira um forma de pagamento valida ')

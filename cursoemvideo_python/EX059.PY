#variaveis
resp = 0

#apresentando o programa 
print('-'*25)
print('Bem vindo a calculadora')
print('-'*25)

#declarando funções da calculadora
def soma(num1, num2):
    valor_somado = num1 + num2
    return valor_somado

def subtracao(num1, num2):
    valor_somado = num1 - num2
    return valor_somado

def multiplicacao(num1, num2):
    valor_somado = num1 * num2
    return valor_somado

def divisao(num1, num2):
    valor_somado = num1 / num2
    return valor_somado

#iniciando a calculadora
while resp != 5:

    print('Selecione sua operação: ')
    print('[1] Soma')
    print('[2] Subtrair')
    print('[3] multiplicar')
    print('[4] dividir')
    print('[5] Sair')
    resp = int(input(":"))

    #tratando entradas
    if resp > 5 or resp < 0:
        print('Por favor insira uma operação valida [1 a 5]')
        break

    if resp != 5:
        x = int(input(('Digite o primeiro valor: ')))
        y  = int(input(('Digite o segundo valor: ')))

    
    #verificando entrada e fazendo a operação
    match resp:

        case 1:
            print('O valor da sua operação é', soma(x, y))
        case 2:
            print('O valor da sua operação é', subtracao(x, y))
        case 3:
            print('O valor da sua operação é', multiplicacao(x, y))
        case 4:
            print('O valor da sua operação é', divisao(x, y))
        case 5:
            print('Encerrando o programa...')
            break

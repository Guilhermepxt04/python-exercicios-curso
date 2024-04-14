
#valor = int(input('Digite até quanto vai contar: '))
#contador = 0
#
#while (contador <= valor - 1):
#    soma = int(input('digite uma valor para somar: '))
#    contador = contador + soma
#    print(contador)
#    if contador > valor:
#        print('Você quebrou meus limites :( ')
#print('fim do contador ')

contador = 1
soma = 0
maior = 0
menor = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999


while (contador <= 3):
    valor = int(input(f'Digite o {contador}. valor: '))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    soma = soma + valor
    contador = contador + 1
print(f'o valor de tudo somado foi de {soma}')
print(f'E o maior valor digitado foi de {maior}')
print(f'E o menor valor digitado foi de {menor}')

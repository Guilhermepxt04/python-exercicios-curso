#recursos
cores = { 'limpa' : '\033[m',
'verde' : '\033[4;32m',
'vermelho' : '\033[4;31m',
'amarelo' : '\033[4;33m' ,}

#variaveis
weight = float(input('Digite seu peso em KG: '))
heigt = float(input('digite sua altura metros: '))
imc = weight / heigt ** 2

print(f'Seu imc está em {cores["amarelo"]}{imc:.1f}{cores["limpa"]}')

#logica
if imc < 17:
        print(f'{cores["vermelho"]}você está muito abaixo do peso')
elif 17 < imc < 18.5 :
                print(f'{cores["amarelo"]}você está abaixo do peso')
elif 18.5 < imc < 25 :
                        print(f'{cores["verde"]}você está no peso ideal')
elif 25 < imc < 30 :
                                print(f'{cores["amarelo"]}você está com sobrepeso')
elif 30 < imc < 35 :
                                        print(f'{cores["vermelho"]}você está com obesidade')
elif 35 < imc < 40 :
                                                print(f'{cores["vermelho"]}você está com obesidade severa')
else:
        print(f'{cores["vermelho"]}você está com obesidade morbida')

#variaveis
peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
imc =  float(peso / altura ** 2)

print(f'seu imc está em {imc:.2f}')

#logica
if imc < 17:
        print('você está muito abaixo do peso')
elif 17 < imc < 18.5 :
                print('você está abaixo do peso')
elif 18.5 < imc < 25 :
                        print('você está no peso ideal')
elif 25 < imc < 30 :
                                print('você está com sobrepeso')
elif 30 < imc < 35 :
                                        print('você está com obesidade')
elif 35 < imc < 40 :
                                                print('você está com obesidade severa')
else:
        print('você está com obesidade morbida')

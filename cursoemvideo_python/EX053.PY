frase = str(input('Digite uma frase: ')).upper().split()
frase = "".join(frase)
palindromo = frase[::-1]

if palindromo == frase:
    print(palindromo)
    print('é um palindromo')
else:
    print(palindromo)
    print('Não é um palindromo')
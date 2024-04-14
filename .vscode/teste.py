import random, string
senha = ''
tamanho = int(input('Qual o tamanho da senha?: '))

while True:
    caracter = random.choice(string.ascii_letters + string.digits + string.punctuation)
    senha += caracter

    if len(senha) == tamanho:
        break

print(senha)

primeiro_termo = int(input('Digite o primeiro termo de sua PA: '))
razao = int(input('Digite a razão de sua PA: '))
decimo = primeiro_termo + (10 - 1) * razao
for c in range(primeiro_termo, decimo + razao, razao):
    print(c)
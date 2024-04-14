flag = 0
s = 0
c = 0

while flag != 999:
    n = int(input('Digite um numero [999 para parar]: '))
    flag = n
    s += n
    c += 1
print(f'Você digitou {c - 1} valores e a soma entre eles foi {s - flag}')
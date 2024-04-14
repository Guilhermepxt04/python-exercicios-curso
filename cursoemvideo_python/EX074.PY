from random import randint

x0 = randint(0, 100)
x1 = randint(0, 100)
x2 = randint(0, 100)
x3 = randint(0, 100)
x4 = randint(0, 100)

n = (x0, x1, x2, x3, x4)
sorted_n = sorted(n)

print(sorted_n)

print(f'o menor valor é {sorted_n[0]} e o maior valor é {sorted_n[4]}')
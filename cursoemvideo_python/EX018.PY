import math

angulo = float(input('digite um angulo: '))
angulora = math.radians(angulo)
seno = math.sin(angulora)
cosseno = math.cos(angulora)
tangente = math.tan(angulora)
print(f'o angulo de {angulo} tem o seno de {seno:.2f} \no cosseno de {cosseno:.2f} \ne a tangente de {tangente:.2f} ')
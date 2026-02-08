import math

angulo = float(input('Digite o ângulo do seno: '))

Sn = math.sin(math.radians(angulo))
Cs = math.cos(math.radians(angulo))
Tg = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo} tem o seno de {Sn:.2f}')
print(f'O ângulo de {angulo} tem o seno de {Cs:.2f}')
print(f'O ângulo de {angulo} tem o seno de {Tg:.2f}')
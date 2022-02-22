import math

angulo = float(input('Digite o ângulo que você deseja: '))

an = math.radians(angulo)

seno = math.sin(an)
cosseno = math.cos(an)
tan = math.tan(an)

print(f'O ângulo de {angulo} tem o SENO de {round(seno, 2)}')
print(f'O ângulo de {angulo} tem o COSSENO de {round(cosseno, 2)}')
print(f'O ângulo de {angulo} tem o TANGENTE de {round(tan, 2)}')

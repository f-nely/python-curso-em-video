import math

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

# h = math.pow(cateto_oposto, 2) + math.pow(cateto_adjacente, 2)
# print(f'A hipotenusa vai medir {math.sqrt(h)}')

h = math.hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa vai medir {round(h, 2)}')

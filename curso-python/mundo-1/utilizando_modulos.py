# import math
from math import sqrt

num = int(input('Digite um número: '))

raiz = sqrt(num)

# print(f'A raiz de {num} é igual a {math.ceil(raiz)}')
# print(f'A raiz de {num} é igual a {math.floor(raiz)}')
print(f'A raiz de {num} é igual a {round(raiz, 2)}')

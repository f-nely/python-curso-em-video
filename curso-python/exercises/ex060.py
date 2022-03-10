# from math import factorial
#
# print('Digite um número para')
# num = int(input('calcular seu Fatorial: '))
#
# f = factorial(num)
# print(f'O fatorial de {num} é {f}')

num = int(input('calcular seu Fatorial: '))

j = num
f = 1
print(f'Calculando {num}! = ', end='')
while j > 0:
    print(f'{j}', end='')
    print(' x ' if j > 1 else ' = ', end='')
    f *= j
    j -= 1
print(f'{f}')

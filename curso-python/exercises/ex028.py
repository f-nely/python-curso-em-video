from random import randint

num = int(input('Vou pensar em um número entre 0 e 5. Tente adivinhar.. '))

num_aleatorio = randint(0, 5)

print('Processando..')

if num == num_aleatorio:
    print('Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {num_aleatorio} e não no {num}!')

# print(num_aleatorio)

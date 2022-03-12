# j = 1
# while j <= 10:
#     print(f'{j} - ', end='')
#     j += 1
# print('Acabou!')

n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n

print(f'A soma vale {s}')

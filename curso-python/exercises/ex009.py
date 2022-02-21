num = int(input('Digite um número para ver sua tabuada: '))

print('=' * 12)

for i in range(0, 11):
    print(f'{num} x {i} = {num * i}')

print('=' * 12)

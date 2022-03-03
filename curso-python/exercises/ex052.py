qt = 0
num = int(input('Digite um número: '))

for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end='')
        qt += 1
    else:
        print('\033[31m', end='')
    print(i, end=' ')

print(f'\n\033[mO número {num} foi divisível {qt} vezes')
if qt == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

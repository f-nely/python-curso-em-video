# j = 0
# while j <= 10:
#     print(j)
#     j += 1
# print('FIM')

# n = 1
# while n != 0:
#     n = int(input('Digite um valor: '))
# print('FIM')

# r = 'S'
# while r == 'S':
#     n = int(input('Digite um valor: '))
#     r = str(input('Quer continuar? [S/N] ')).upper()
# print('FIM')

qtd_par = qtd_impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            qtd_par += 1
        else:
            qtd_impar += 1
print(f'Você digitou {qtd_par} números pares e {qtd_impar} números ímpares!')
print('ACABOU')

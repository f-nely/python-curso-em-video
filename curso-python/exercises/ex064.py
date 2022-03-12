s = qtd = 0
n = int(input('Digite um número [999 para parar]: '))

while n != 999:
    if n == 999:
        continue
    s += n
    qtd += 1
    n = int(input('Digite um número [9999 para parar]: '))
print(f'Você digitou {qtd} números e a soma entre eles foi {s}')

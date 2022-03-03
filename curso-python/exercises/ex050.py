soma = qt = 0
for i in range(1, 7):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        qt += 1
        soma += num

print(f'Você informou {qt} PARES e a soma foi {soma}')

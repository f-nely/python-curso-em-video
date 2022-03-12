media = qtd = soma = maior = 0
menor = 99
resp = 'S'

while resp != 'N':
    n = int(input('Digite um número: '))
    qtd += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resp = str(input('Quer continuar? ')).upper()
    if resp == 'N':
        continue

media = soma / qtd

print(f'Você digitou {qtd} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

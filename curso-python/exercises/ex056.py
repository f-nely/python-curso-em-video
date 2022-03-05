
media = maior = qtd = soma_idade = 0
nome_mais_velho = ''
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).upper()
    soma_idade += idade
    if sexo == 'M':
        if idade > maior:
            maior = idade
            nome_mais_velho = nome
    if sexo == 'F':
        if 0 < idade < 20:
            qtd += 1
media = soma_idade / 4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {maior} anos e se chama {nome_mais_velho}.')
print(f'Ao todo são {qtd} mulheres com menos de 20 anos')

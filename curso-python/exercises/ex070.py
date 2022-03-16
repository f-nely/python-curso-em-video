print('-' * 30)
print('\t  LOJA SUPER BARATÃO')
print('-' * 30)

tot_compra = p_mmil = menor = cont = 0
nome_p_barato = ''
while True:
    nome_produto = str(input('Nome do Produto: ')).capitalize()
    preco = float(input('Preço: R$ '))
    cont += 1
    tot_compra += preco

    if preco > 1000:
        p_mmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        nome_p_barato = nome_produto

    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break

print('-' * 30)
print(f'O total da compra foi R${tot_compra:.2f}')
print(f'Temos {p_mmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_p_barato} que custa R${menor}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))

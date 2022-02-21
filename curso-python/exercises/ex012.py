preco_produto = float(input('Qual é o preço do produto? R$ '))

# desconto = preco_produto * 0.05
novo_preco = preco_produto - (preco_produto * 0.05)

print(f'O produto que custava R${preco_produto}, na promoção '
      f'com desconto de 5% vai custar R$ {round(novo_preco, 2)}')

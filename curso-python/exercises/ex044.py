valor_compra = float(input('Preço das compras: R$ '))

print('''FORMAS DE PAGAMENTOS
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')

op = int(input('Qual é a opção? '))

if op == 1:
    valor_final = valor_compra - (valor_compra * 0.1)
elif op == 2:
    valor_final = valor_compra - (valor_compra * 0.05)
elif op == 3:
    valor_final = valor_compra
    parcela = valor_compra / 2
    print(f'Sua compra será parcelada em 2x de R${parcela} SEM JUROS')
elif op == 4:
    valor_final = valor_compra + (valor_compra * 0.2)
    qtd_parcelas = int(input('Quantas parcelas? '))
    parcela = valor_final / qtd_parcelas
    print(f'Sua compra será parcelada em {qtd_parcelas}x de R${parcela} COM JUROS')
else:
    valor_final = valor_compra
    print('Opção INVÁLIDA de pagamento.')
print(f'Sua compra de R${valor_compra} vai custar R${valor_final} no final.')

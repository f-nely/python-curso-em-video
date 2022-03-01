valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = valor_casa / (anos * 12)
print(f'Para pagar uma casa de R${valor_casa} em {anos} anos a prestação será de R${round(prestacao, 2)} ')

# print(salario * 0.3)
if prestacao <= salario * 0.3:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')

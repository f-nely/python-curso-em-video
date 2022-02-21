salario = float(input('Qual é o salário do funcionário? R$ '))

novo_salario = salario + (salario * 0.15)

print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${round(novo_salario, 2)}')

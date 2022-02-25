salario = float(input('Qual é o salário do funcionário? R$ '))

if salario <= 1250:
    novo_salario = salario + (salario * 0.15)
else:
    novo_salario = salario + (salario * 0.1)

print(f'Quem ganhava R${salario} passa a ganhar R${novo_salario} agora.')

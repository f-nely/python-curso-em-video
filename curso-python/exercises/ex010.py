real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = 5.08

print(f'Com R${real} você pode comprar US${round(real / dolar, 2)}')

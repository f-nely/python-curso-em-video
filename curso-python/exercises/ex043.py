peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa é de {round(imc, 1)}')

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif imc >= 18.5 and imc < 25:
    print('Parabéns, Você está na faixa de PESO NORMAL')
elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')

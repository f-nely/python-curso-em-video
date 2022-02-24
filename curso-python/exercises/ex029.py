velocidade = float(input('Qual é a velocidade atual do carro? '))

# print(velocidade)
if velocidade > 80:
    # velocidade_excedente = velocidade - 80
    # print(velocidade_excedente)
    # valor_multa = velocidade_excedente * 7
    # print(valor_multa)
    multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    # print(f'Você deve pagar uma multa de R${valor_multa}!')
    print(f'Você deve pagar uma multa de R${multa}!')

print('Tenha um boa tarde! Dirija com segurança!')

frase = str(input('Digite uma frase: ')).strip().upper()

format_frase = frase.replace(' ', '')
inversa = format_frase[::-1]
# print(inversa)

if format_frase == inversa:
    print(f'O inverso de {format_frase} é {inversa}')
    print('Temos um palíndromo!')
else:
    print(f'O inveso de {format_frase} é {inversa}')
    print('A frase digitada não é um palíndromo!')

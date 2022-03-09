from random import randint

numero_aleatorio = randint(0, 10)

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')

acertou = False
palpites = 0
while not acertou:
    num = int(input('Qual é seu palpite? '))
    palpites += 1
    if num == numero_aleatorio:
        acertou = True
    else:
        if num < numero_aleatorio:
            print('Mais... Tente mais uma vez.')
        elif num > numero_aleatorio:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')

from random import choice
from time import sleep

my_list = ['papel', 'tesoura', 'pedra']

computador = choice(my_list)

print('''Suas opções:
PEDRA
PAPEL
TESOURA''')

jogador = str(input('Qual é a sua jogada? ')).strip().lower()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

print('-=' * 11)
print(f'Computador jogou {computador}')
print(f'Jogador jogou {jogador}')
print('-=' * 11)

if computador == 'pedra' and jogador == 'tesoura':
    print('O camputador ganhou')
elif computador == 'tesoura' and jogador == 'papel':
    print('O camputador ganhou')
elif computador == 'papel' and jogador == 'pedra':
    print('O camputador ganhou')
elif jogador == 'pedra' and computador == 'tesoura':
    print('O jogador ganhou')
elif jogador == 'tesoura' and computador == 'papel':
    print('O jogador ganhou')
elif jogador == 'papel' and computador == 'pedra':
    print('O jogador ganhou')
else:
    print('empate')

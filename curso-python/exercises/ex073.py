print('-=' * 15)

brasileirao = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
               'América-MG', 'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Atlético-PR',
               'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')

print(f'Lista de times do Brasileirão: {brasileirao}')
print('-=' * 15)
print(f'Os 5 primeiros são {brasileirao[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {brasileirao[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-=' * 15)
posicao_chap = brasileirao.index('Chapecoense')
print(f'O Chapecoense está na {posicao_chap+1}ª posição')

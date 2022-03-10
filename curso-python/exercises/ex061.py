print('Gerador de PA')
print('-=' * 10)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

j = 0
while j < 10:
    print(primeiro_termo + j * razao, end=' - ')
    j += 1

print('FIM')

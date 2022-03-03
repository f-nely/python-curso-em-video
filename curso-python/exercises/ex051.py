print('=' * 30)
print('\t 10 TERMOS DE UMA PA')
print('=' * 30)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(0, 10):
    print(primeiro_termo + i * razao, end=' → ')

print('ACABOU')

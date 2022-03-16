print('-' * 30)
print('CADASTRE UMA PESSOA')
print('-' * 30)

total = qtd_h = m = 0

while True:
    idade = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F] ')).upper()

    if idade >= 18:
        total += 1
    if s == 'M':
        qtd_h += 1
    if s == 'F' and idade < 20:
        m += 1

    opt = ' '
    while opt not in 'SN':
        opt = str(input('Quer continuar? [S/N] ')).upper()

    if opt == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {total}')
print(f'Ao todo temos {qtd_h} homens cadastrados: ')
print(f'E temos {m} mulheres com menos de 20 anos')

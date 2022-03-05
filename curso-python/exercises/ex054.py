from datetime import date

ano_atual = date.today().year

qtd_maior = qtd_menor = 0
for i in range(1, 8):
    nasc = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    idade = ano_atual - nasc
    if idade >= 21:
        qtd_menor += 1
    else:
        qtd_maior += 1

print(f'Ao todo tivemos {qtd_maior} pessoas maiores de idade')
print(f'E também tivemos {qtd_menor} pessoas menores de idade')

from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))
s = str(input('''Digite 
[ M ] - para masculino
[ F ] - para feminino
''')).strip().capitalize()

ano_atual = date.today().year

idade = ano_atual - ano_nascimento

# al = 18 - idade
# print(al)
# an_al = ano_atual + al
# print(an_al)

print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')

if idade == 18 and s == 'M':
    print(f'Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18 and s == 'M':
    saldo = 18 - idade
    alistamento = ano_atual + saldo
    # print(f'Ainda faltam {al} anos para o alistamento.')
    # print(f'Seu alistamento será em {an_al}.')
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    print(f'Seu alistamento será em {alistamento}.')
elif idade > 18 and s == 'M':
    saldo = idade - 18
    alistamento = ano_atual - saldo
    # print(f'Você já deveria ter se alistado há {abs(al)} anos.')
    # print(f'Seu alistamento foi em {an_al}.')
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi em {alistamento}.')
else:
    print('Alistamento obrigatório é somente para homens.')

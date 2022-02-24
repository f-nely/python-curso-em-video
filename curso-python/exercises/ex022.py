full_name = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome em maiúsculas é {full_name.upper()}')
print(f'Seu nome em minúsculas é {full_name.lower()}')
name_without_space = full_name.replace(' ', '')
print(f'Seu nome tem ao todo {len(name_without_space)} letras')
# print(full_name.split())
lista = full_name.split()
first_name = lista[0]
print(f'Seu primeiro nome é {first_name} e ele tem {len(first_name)} letras')
# print(full_name.replace(' ', ''))

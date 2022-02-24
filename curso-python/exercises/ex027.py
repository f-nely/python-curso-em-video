name = str(input('Digite seu nome completo: ')).strip()

print('Muito prazer em te conhecer!')
list_name = name.split()
# print(list_name)
first_name = list_name[0]
# print(list_name[0])
# print(len(name.split()))
index = len(name.split())
last_name = list_name[index - 1]
# print(index)
# print(f'Seu primeiro nome é {first_name}')
# print(f'Seu último nome é {last_name}')

print(f'Seu primeiro nome é {list_name[0]}')
print(f'Seu último nome é {list_name[len(list_name)-1]}')

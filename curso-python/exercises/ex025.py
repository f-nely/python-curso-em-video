full_name = str(input('Qual é seu nome completo? ')).strip().title()

print(full_name)
result = full_name.find('Silva') != -1
# print(full_name.find('Silva') != -1)
# print(f"Seu nome tem Silva? {result}")
print(f"Seu nome tem Silva? {'Silva' in full_name}")

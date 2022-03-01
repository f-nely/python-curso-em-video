name = str(input('Qual é o seu nome? ')).capitalize()

if name == 'Gustavo':
    print('Que nome bonito!')
elif name == 'Pedro' or name == 'Maria' or name == 'Elzo':
    print('Seu nome é bem popular no Brasil.')
elif name in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {name}!')

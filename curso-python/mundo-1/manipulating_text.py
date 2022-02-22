frase = 'Curso em Vídeo Python'

# fatiamento de string
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

# análise de string
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

# transformação de string
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = '   Aprenda Python  '
print(len(frase2))
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

# divisão de string
print(frase.split())
print('-'.join(frase))

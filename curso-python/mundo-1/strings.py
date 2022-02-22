frase = 'Curso em Vídeo Python'
# frase = '  Curso em Vídeo Python  '

print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

print("""Learn Python
Python is a popular programming language.
Python can be used on a server to create web applications.""")

print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'PHP'))
print('Curso' in frase)
print(frase.find('Vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])

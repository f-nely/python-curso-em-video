f = str(input('Digite uma frase: ')).strip().lower()

# print(f)
print(f"A letra A aparece {f.count('a')} vezes na frase.")
print(f"A primeira letra A apareceu na posição {f.find('a') + 1}")
print(f"A última letra A apareceu na posição {f.rfind('a') + 1}")

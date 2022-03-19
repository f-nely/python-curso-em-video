# as tuplas são imutáveis
lanches = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

print(type(lanches))
print(lanches[2])
print(lanches[0:2])
print(lanches[1:])
print(lanches[-1])
print(lanches[-2])
print(lanches[1:3])
print(lanches[-3:])
print(len(lanches))
print(lanches)

for cont, lanche in enumerate(lanches):
    print(f'Eu vou comer {lanche} na posição {cont}')

lanches2 = ('pastel', 'bolo', 'refrigerante', 'caldo de cana', 'cachorro quente')
print(lanches2)
print(sorted(lanches2))

par = (4, 2, 6, 8)
impar = (7, 3, 5)
numeros = par + impar
print(numeros)
print(numeros.count(5))
print(numeros.index(4))

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
del pessoa

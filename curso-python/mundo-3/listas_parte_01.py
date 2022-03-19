lanche = ['hambúrguer', 'suco', 'pizza', 'pudim']

print(lanche)
print(lanche[2])
lanche[3] = 'picole'
lanche.append('cookie')
lanche.insert(0, 'cachorro quente')
print(lanche)
# del lanche[3]
# lanche.pop(3)
lanche.remove('pizza')
lanche.pop()
print(lanche)
if 'pizza' in lanche:
    lanche.remove('pizza')

valores = list(range(4, 11))
print(valores)

values = [8, 2, 5, 4, 9, 3, 0]
print(values)
print(sorted(values))
print(len(values))

num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
# num.pop()
# num.pop(2)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(2, 2)
print(num)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4!')
print(num)

numeros = list()
numeros.append(5)
numeros.append(9)
numeros.append(4)

for c, v in enumerate(numeros):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

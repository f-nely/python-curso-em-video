soma = qt = 0
for i in range(1, 501, 2):
    # if i % 2 == 0:
    #     continue
    # print(i)
    if i % 3 == 0:
        qt += 1
        soma += i

# print(qt, soma)
print(f'A soma de todos os {qt} valores solicitados é {soma}')

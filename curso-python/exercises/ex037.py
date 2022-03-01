num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opt = int(input('Sua opção: '))

if opt == 1:
    # binario = format(num, 'b')
    # print(binario)
    # print(bin(num)[2:])
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opt == 2:
    # octal = format(num, 'o')
    # print(octal)
    # print(oct(num)[2:])
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opt == 3:
    # hexa = format(num, 'x')
    # print(hexa)
    # print(hex(num)[2:])
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida!')

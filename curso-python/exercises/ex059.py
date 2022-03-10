from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

opt = 0

while opt != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programas''')

    opt = int(input('>>>>> Qual é a sua opção? '))

    if opt == 1:
        print(f'A soma entre {num1} + {num2} é {num1 + num2}')
    elif opt == 2:
        print(f'A multiplicação entre {num1} * {num2} é {num1 * num2}')
    elif opt == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        elif num1 == num2:
            print(f'{num1} é igual a {num2}')
        else:
            print(f'{num2} é maior que {num1}')
    elif opt == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opt == 5:
        print('Finalizando...')
    else:
        print('Opção inválida!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')

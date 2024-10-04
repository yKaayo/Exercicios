num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

option = 0

while option != 5:
    print(' =/==/= ' * 5)
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    print(' =/==/= ' * 5)

    option = int(input('Qual sua opção? '))

    if option == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif option == 2:
        print(f'{num1} x {num2} = {num1 * num2}')
    elif option == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        else:
            print(f'{num1} é menor que {num2}')
    elif option == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
    else:
        print('Opção inválida')

print('O programa foi encerrado!')
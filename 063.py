result = 0
num1 = 1
num2 = 0

print('Sequência de Fibonacci')

num = int(input('Quantos termos você quer mostrar: '))

for a in range(0, num):
    result = num1 + num2
    print(f'{result} -> ', end='')

    num1 = num2
    num2 = result

print('Fim')

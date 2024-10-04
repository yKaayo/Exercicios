result = 1

factorial = int(input('Digite um número para calcular seu fatorial: '))

print(f'{factorial}! =', end=' ')

for num in range(factorial, 0, -1):
    result *= num

    print(num, end='')
    print(' x ' if num != 1 else '', end='')

print(f' = {result}')

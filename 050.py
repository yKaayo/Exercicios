sum = 0

for a in range(1, 7):
    num = int(input(f'Digite um valor: '))

    if num % 2 == 0:
        sum += num

print(f'A soma dos valores pares são: {sum}')
number = int(input('Digite um número para ver sua tabuada: '))

for tabuada in range(0, 11, 1):
    print(f'{number} x {tabuada} = {number * tabuada}')
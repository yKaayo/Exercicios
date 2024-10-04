high = 0
light = 0

for num in range(1, 6):
    weight = float(input(f'Qual o peso da {num}° pessoa? '))

    if num == 1:
        high = weight
        light = weight
    else:
        if weight > high:
            high = weight
        if weight < light:
            light = weight

if high == light:
    print(f'O maior e menor peso são {high}Kg')
else:
    print(f'O maior peso foi {high}Kg')
    print(f'O menor peso foi {light}Kg')
    
from datetime import date

kid = 0
old = 0

for num in range(1, 8):
    year = int(input(f'Em que ano a {num}° pessoa nasceu: '))

    age = date.today().year - year

    if age >= 18:
        old += 1
    elif age < 18:
        kid += 1

print(f'Há {old} maiores de idade')
print(f'Há {kid} menores de idade')
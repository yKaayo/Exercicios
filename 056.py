average = 0
old = 0
woman = 0
oldName = ''

for num in range(1, 5):
    print(f'---- {num}° Pessoa ----')
    name = input('Nome: ')
    age = int(input('Idade: '))
    sex = input('Sexo [M/F]: ').lower().strip()

    average += age / 4

    if sex == 'm' and old < age:
        old = age
        oldName = name

    if sex == 'f' and age < 18:
        woman += 1

print(f'A média de idade é {average} anos')
print(f'O homem mais velho tem {old} anos')
print(f'Há {woman} mulheres com menos de 18 anos e se chama {oldName}')

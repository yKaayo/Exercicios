withdrew = int(input('Quanto você quer sacar? R$'))
money = withdrew
count = 0

while money <= withdrew:
    while withdrew >= 100:
        withdrew -= 100
        count += 1
    print(f'Total de {count} cédulas de R$100')
    count = 0

    while withdrew >= 50 and  withdrew < 100:
        withdrew -= 50
        count += 1
    print(f'Total de {count} cédulas de R$50')
    count = 0

    while withdrew >= 20 and  withdrew < 50:
        withdrew -= 20
        count += 1
    print(f'Total de {count} cédulas de R$20')
    count = 0

    while withdrew >= 10 and  withdrew < 20:
        withdrew -= 10
        count += 1
    print(f'Total de {count} cédulas de R$10')
    count = 0

    while withdrew >= 1 and  withdrew < 10:
        withdrew -= 1
        count += 1
    print(f'Total de {count} cédulas de R$1')
    count = 0
  
from datetime import date

born = int(input('Ano de nascimento: '))

year = date.today().year
age = date.today().year - born

print(f'Quem nasceu em {born} tem {age} anos em {year}')

if age < 18:
    left = 18 - age
    if left == 1:
        print(f'Ainda falta {left} ano para o alistamento militar') #Singular
    else:
        print(f'Ainda faltam {left} anos para o alistamento militar') #Plural
        print(f'Seu alistamento será em {year + left}')
elif age == 18:
    print(f'Você deve alistar esse ano')
else:
    past = year - born - 18
    yearEnlistment = born + 18
    if past == 1:
        print(f'Você foi alistado há {past} ano atrás') #Singular
        print(f'Seu alistamento foi em {yearEnlistment}')
    else:
        print(f'Você foi alistado há {past} anos atrás') #Plural
        print(f'Seu alistamento foi em {yearEnlistment}')
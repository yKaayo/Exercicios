stuff = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(stuff)}')
print(f'Só tem espaços? {stuff.isspace()}')
print(f'É um número? {stuff.isnumeric()}')
print(f'É alfabético? {stuff.isalpha()}')
print(f'É alfanumérico? {stuff.isalnum()}')
print(f'Está em maiúscula? {stuff.isupper()}')
print(f'Está em minúscula? {stuff.islower()}')
print(f'Está capitalizada? {stuff.istitle()}')
name = input('Digite seu nome completo: ')

newName = name.split()

print(f'Seu primeiro nome é {newName[0]}')
print(f'Seu último nome é {newName[len(newName) - 1]}')
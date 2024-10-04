name = input('Digite seu nome completo: ').strip()

print('Analisando seu nome...')

newName = name.split()

print(f'Seu nome em maiúscula é {name.upper()}')
print(f'Seu nome em minúscula é {name.lower()}')
print(f'Seu nome tem ao todo {len(name) - name.count(' ')} letras')
print(f'Seu primeiro nome é {newName[0]} e ele tem {name.find(' ')} letras')

from random import shuffle

first = input('Primeiro aluno: ')
second = input('Segundo aluno: ')
third = input('Terceiro aluno: ')
fourth = input('Quarto aluno: ')

studants = [first, second, third, fourth]
shuffle(studants)

print(f'A ordem é {studants}')
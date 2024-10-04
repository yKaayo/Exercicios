import random

first = input('Primeiro aluno: ')
second = input('Segundo aluno: ')
third = input('Terceiro aluno: ')
fourth = input('Quarto aluno: ')

studants = [first, second, third, fourth]
choice = random.choice(studants)

print(f'O aluno escolhido foi {choice}')
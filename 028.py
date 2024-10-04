from random import randint

print('Eu vou pensar em um número entre 0 e 5. Tente adivinhar...')
number = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')

rightNumber = randint(0, 5)

if rightNumber == number:
    print(f'Você ganhou! O número escolhido foi {rightNumber}')
else:
    print(f'Você perdeu! O número escolhido foi {rightNumber}')
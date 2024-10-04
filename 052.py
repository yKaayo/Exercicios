import colorama
from colorama import Fore

divided = 0

num = int(input('Digite um número: '))


for a in range(1, num + 1):

    if num % a == 0:
        divided += 1
        print(Fore.RED + f'{a}' + Fore.RESET, end=' ')
    else:
        print(f'{a}', end=' ')

print(f'\nO número {num} foi divisível {divided} vezes')

if divided == 2:
    print(f'{num} é primo!')
else:
    print(f'{num} não é primo!')

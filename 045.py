import random 

print('Suas opções:')

print('[ 0 ] Pedra')
print('[ 1 ] Papel:')
print('[ 2 ] Tesoura:')

choice = input('Qual a sua jogada? ')

if choice == '0':
    choice = 'pedra'
elif choice == '1':
    choice = 'papel'
elif choice == '2':
    choice = 'tesoura'
else:
    print('Opção inválida')

options = ['pedra', 'papel', 'tesoura']
option = random.choice(options)

if option == choice:
    print(f'Empatou! Você escolheu {choice} e a maquina {option}')
elif choice == 'pedra':
    if option == 'papel':
        print(f'Perdeu! Você escolheu {choice} e a maquina {option}')
    elif option == 'tesoura':
        print(f'Ganhou! Você escolheu {choice} e a maquina {option}')
elif choice == 'papel':
    if option == 'pedra':
        print(f'Ganhou! Você escolheu {choice} e a maquina {option}')
    elif option == 'tesoura':
        print(f'Perdeu! Você escolheu {choice} e a maquina {option}')
elif choice == 'tesoura':
    if option == 'pedra':
        print(f'Perdeu! Você escolheu {choice} e a maquina {option}')
    elif option == 'papel':
        print(f'Ganhou! Você escolheu {choice} e a maquina {option}')

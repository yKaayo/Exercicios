from random import randint

tries = 1

rightNumber = randint(1, 10)

print('Pensei em um número de 0 à 10')
num = int(input('Qual seu palpite? '))

while num != rightNumber:
    tries += 1
    if num > rightNumber:
        num = int(input('Errou! Tente novamente um número menor: '))
    else:
        num = int(input('Errou! Tente novamente um número maior: '))

if tries == 1:
    print(f'Acertou! O número é {rightNumber} em {tries} tentativa') #Singular
else:
    print(f'Acertou em {tries} tentativas! O número é {rightNumber}!') #Plural

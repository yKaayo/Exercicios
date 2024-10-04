num = 0
nums = 0
sum = 0

while num != 999:
    num = int(input('Digite um número: [999 para sair] '))

    if num != 999:
        nums += 1
        sum += num 

print(f'Você digitou {nums} números e sua soma é {sum}')

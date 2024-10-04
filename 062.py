firstTerm = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
lastTerm = (firstTerm + 9 * reason) + reason

newNum = 1
total = 0

while newNum != 0:
    for num in range(firstTerm, lastTerm, reason):
        print(f'{num} ->', end=' ')
        total += 1
    
    print('Pausa')
    
    newNum = int(input('Quantos termos você quer mostrar a mais? '))
    if newNum != 0:
        firstTerm = lastTerm
        lastTerm = firstTerm + newNum * reason

print(f'Um total de {total} termos')
print('Encerrado')

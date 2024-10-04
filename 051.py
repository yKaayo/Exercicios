term = int(input('Digite o primeiro termo: '))
reason = int(input('Digite a razão: '))
lastTerm = (term + 9 * reason) + reason

for num in range(term, lastTerm, reason):
    print(f'{num} ->', end=' ')

print('Finished')
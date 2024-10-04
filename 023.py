number = int(input('Digite um número: '))

print(f'Analisando o numero {number}')

u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print(f'Unidade {u}')
print(f'Dezena {d}')
print(f'Centana {c}')
print(f'Milhar {m}')
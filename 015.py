day = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))

price = (day * 60) + (km * 0.15)

print(f'O total a pagar é de R${price:.2f}')
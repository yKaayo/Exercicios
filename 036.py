value = float(input('Valor da casa: R$'))
wage = float(input('Salário do comprador: R$'))
year = int(input('Quantos anos de financiamento? '))

installment = value / (year * 12)

print(f'Para pagar uma casa de {value:.2f} em {year} anos a prestação será de R${installment:.2f}')

if installment <= wage * 0.3:
    print('Empréstimo aceito')
else:
    print('Empréstimo negado')
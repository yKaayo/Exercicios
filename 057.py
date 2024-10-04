sex = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sex not in 'MF':
    sex = str(input('Dados inválidos! Informe novamente seu sexo: ')).strip().upper()[0]

print('Dados Válidos!')

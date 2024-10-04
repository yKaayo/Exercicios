width = float(input('Largura da parede: '))
height = float(input('Altura da parede: '))

area = height * width
litro = (area) / 2

print(f'Sua parede tem a dimensão de {width} x {height} e a sua área é de {area:.2f}m².')
print(f'Para pintar sua parede, você precisará de {litro:.2f}L tinta.')
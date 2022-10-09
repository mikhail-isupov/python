# По заданному номеру четверти плоскости выводит диапазоны координат
sector = None
sectors = ('1', '2', '3', '4')
range_of_coordinates = {'1' : 'x > 0, y > 0', '2' : 'x < 0, y > 0', '3' : 'x < 0, y < 0', '4' : ' x > 0, y < 0'}

while sector not in sectors:
    sector = input('Введите номер четверти 1..4: ')

print(f'Четверть плоскости N {sector} соответствует координатам {range_of_coordinates[sector]}')

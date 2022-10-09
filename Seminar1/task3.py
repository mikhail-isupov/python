# Определение номера четверти плоскости
x = float(input('Введите координату X '))
y = float(input('Введите координату Y '))
sector = None

if x > 0 and y > 0:
    sector = 1
elif x < 0 and y > 0:
    sector = 2
elif x < 0 and y < 0:
    sector = 3
elif x > 0 and y < 0:
    sector = 4

if sector is None:
    if x == 0 and y == 0:
        print('Начало координат')
    elif x != 0:
        print('Ось X')
    else:
        print('Ось Y')
else:
    print('Четверть плоскости номер ', sector)
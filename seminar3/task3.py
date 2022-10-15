#Поиск разницы между максимальным и минимальным значением дробной части из списка вещественных чисел
import random as rnd

rnd.seed()

num_list = [round(rnd.random()*10, 2) for i in range(rnd.randint(2,9))]

print('Сгенерированный список вещественных чисел: ', num_list)

max_fract = 0
min_fract = 1

for number in num_list:

    num_fract = number - int(number)

    if num_fract > max_fract:
        max_fract = num_fract

    if num_fract < min_fract:
        min_fract = num_fract

print('Разница между максимальным и минимальным значением дробной части элементов списка: ', round(max_fract - min_fract, 2))

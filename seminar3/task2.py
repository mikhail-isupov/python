#Произведение пар элементов списка
import random as rnd

rnd.seed()

list_len = rnd.randint(2,9)

num_list = [rnd.randint(0,9) for i in range(list_len)]

print('Сгенерированный список: ', num_list)

num_list_multiplied = [ num_list[i]*num_list[-(i + 1)] for i in range(list_len // 2 + list_len % 2) ]

print('Список из попарно умноженных элементов: ', num_list_multiplied)

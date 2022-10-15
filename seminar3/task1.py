#Сумма элементов списка с нечетными индексами
import random as rnd

rnd.seed() # инициализация генератора псевдослучайных чисел

num_list = [rnd.randint(0,9) for i in range(rnd.randint(2,9))]

print('Сгенерированный список: ', num_list)

print('Элементы списка с нечетными индексами: ', num_list[1::2])

print('Их сумма: ',sum(num_list[1::2]))

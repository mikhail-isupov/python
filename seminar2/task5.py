import random as rnd

n = 100
list_of_numbers = [ i for i in range(n) ]
rnd.seed()

print(f'Исходный список из {n} элементов')
print(list_of_numbers)

for i in range(n):
    swap = list_of_numbers[i]
    new_index = rnd.randint(0, n - 1)
    list_of_numbers[i] = list_of_numbers[new_index]
    list_of_numbers[new_index] = swap

print('Перемешанный список')
print(list_of_numbers)

    

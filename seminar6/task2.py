#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности, список повторяемых и убрать дубликаты из заданной последовательности.

data_string = input('Введите последовательность через пробел: ')
data = data_string.split()
elements = set(data)
unique_elements = []
nonunique_elements = []

for element in elements:
    if data.count(element) == 1:
        unique_elements.append(element)
    else:
        nonunique_elements.append(element)

print('Уникальные элементы: ', sorted(unique_elements))
print('Повторяемые элементы: ', sorted(nonunique_elements))
print('Элементы без дубликатов: ', sorted(elements))

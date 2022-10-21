#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

elements = input('Введите последовательность элементов через пробел: ').split()

unique_elements = []

element_to_skip = False

for element in sorted(elements):
    if (not unique_elements or unique_elements[-1] != element) and not element_to_skip:
        unique_elements.append(element)
    elif unique_elements[-1] == element:
        element_to_skip = True
    else:
        unique_elements.pop()
        element_to_skip = False
        unique_elements.append(element)

if element_to_skip:
    unique_elements.pop()

print('Список неповторяющихся элементов: ', unique_elements)
        
    


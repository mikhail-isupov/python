#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k

import random as rnd

k = int(input('Введите степень многочлена k: '))

file_name = input('Введите имя файла для записи многочлена: ')

coeffs = [0] * (k + 1) #у многочлена степени k может быть k + 1 коэффициентов

coeffs[k] = rnd.randint(1, 100) #Иначе это не будет многочлен степени k

zero_coeffs = True

while zero_coeffs:
    for i in range(k):
        coeffs[i] = rnd.randint(0, 100)
        if zero_coeffs and coeffs[i]:
            zero_coeffs = False #Хотя бы один из остальных коэффициентов тоже должен от нуля отличаться

with open(file_name, 'w') as file:
    file.write(" ".join(map(str, coeffs)))

#В файл записываются коэффициенты поскольку для записи многочлена достаточно записать его коэффициенты a0, a1... ak
#Прочитав такой файл и найдя там k + 1 коэффициентов восстанавливаем многочлен степени k
#Отсутствующим степеням соответствуют нулевые значения коэффициентов
        



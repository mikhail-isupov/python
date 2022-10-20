#Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

file_input1 = input('Введите имя первого файла: ')

file_input2 = input('Введите имя второго файла: ')

file_output = input('Введите имя выходного файла: ')

polinom1 = polinom2 = polinom3 = []

with open(file_input1) as file:
    polinom1 = file.read().split()

with open(file_input2) as file:
    polinom2 = file.read().split()

max_len = len(polinom2) if len(polinom2) > len(polinom1) else len(polinom1)

for i in range(max_len):
    coeff1 = coeff2 = 0

    if i < len(polinom1):
        coeff1 = int(polinom1[i])

    if i < len(polinom2):
        coeff2 = int(polinom2[i])

    polinom3.append(coeff1 + coeff2)

with open(file_output, 'w') as file:
    file.write(" ".join(map(str, polinom3)))

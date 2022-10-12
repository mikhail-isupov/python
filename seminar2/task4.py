import random as rnd

n = 0
while n < 1:
    n = int(input('Введите число элементов списка: '))

rnd.seed()

num_list = [rnd.randint(-n, n) for i in range(n)]

print(f'Сгенерированный список из {n} элементов в диапазоне [{-n}, {n}]: ')
print(num_list)

file = open('file.txt')

num_list_product = None

for data in file:
    if n > int(data) >= 0:
        if num_list_product is None:
            num_list_product = num_list[int(data)]
        else:
            num_list_product *= num_list[int(data)]

file.close()

if num_list_product is None:
    print('Ни одного элемента списка не соответствуют фильтру')
else:
    print(f'Произведение элементов списка отфильтрованных в соответствии с файлом = {num_list_product}')

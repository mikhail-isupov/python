n = 0
while n < 1:
    n = int(input('Введите число N >= 1 '))

list_of_factorials = [1]

for i in range(2, n + 1):
    list_of_factorials.append(i * list_of_factorials[-1])

print(f'Список всех факториалов от 1 до N: {list_of_factorials}')

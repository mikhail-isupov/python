m = 0
while m  < 1:
    m = int(input('Введите целое число >= 1: '))

num_list = [ (1 + 1 / n) ** n for n in range(1, m + 1) ]

print('Последовательность (1 + 1/n) ^ n ')
print(num_list)

print(f'Сумма элементов последовательности = {sum(num_list)}')
    

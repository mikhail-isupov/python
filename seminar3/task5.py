#Поиск чисел Фибоначчи в диапазоне -N...N

n = int(input('Введите максимальный индекс числа Фибоначчи n: '))

fibo = [0, 1]

for i in range(n):
    fibo.append(fibo[-1] + fibo[-2])
    fibo.insert(0, fibo[1] - fibo[0])

print('Все числа Фибоначчи F-n...Fn: ', fibo[:-1])

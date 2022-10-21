#Задайте натуральное число N.
#Напишите программу, которая составит список простых множителей числа N.

num = 0
while num < 2:
    num = int(input('Введите целое число N > 1: '))

prime_nums = []

max_multiplier = round (num ** 0.5)

for i in range(1, max_multiplier // 2 + 1):
    index = 2 * i + 1
    
    is_index_prime = True
    
    for prime_num in prime_nums:
        if not (index % prime_num):
            is_index_prime = False

    if is_index_prime:
        prime_nums.append(index)

prime_nums.append(2)

prime_factors = []

for prime_num in prime_nums:
   while not (num % prime_num):
            prime_factors.append(prime_num)
            num //= prime_num

if num > 1:
    prime_factors.append(num)

print('Список простых множителей числа: ', prime_factors)

number = float(input('Введите вещественное число: '))

num_int = int(number)
num_fract = number - num_int
num_sum = 0

while num_int != 0:
    num_extracted = num_int % 10
    num_sum += num_extracted
    num_int = num_int // 10

while num_fract != 0:
    num_extracted = int(num_fract * 10)
    num_sum += num_extracted
    num_fract = round(num_fract * 10 - num_extracted, 14)

print(f'Сумма цифр равна {num_sum}')

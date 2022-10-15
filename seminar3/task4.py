#Показать двоичное представление числа

number = int(input('Введите целое число: '))

output_str = ''

while number:


    digit = number % 2

    output_str = str(digit) + output_str

    number //= 2


print('Двоичное представление числа: ', output_str)

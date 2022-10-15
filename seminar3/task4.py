#Показать двоичное представление числа

number = int(input('Введите целое число: '))

output_str = ''

while number or not output_str:

    digit = number % 2

    output_str = str(digit) + output_str

    number = number // 2

print('Двоичное представление числа: ', output_str)

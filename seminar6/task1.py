#Калькулятор арифметических выражений

def calc(expression, index=None):
#Используется список для создания единого для всех вызовов функции счетчика текущей позиции
    if index is None:
        index = [0]
    number = []
    numbers = []
    operations = []
    digits = ".,0123456789"
    operators = "+-*/"

    while index[0] < len(expression) and expression[index[0]] != ')':
        if expression[index[0]] == '(':#Вычисление выражения в скобках
            index[0]+=1
            numbers.append(calc(expression, index))
        elif expression[index[0]] in digits:#Чтение числа
            number.append(expression[index[0]])
        elif expression[index[0]] in operators:#Чтение оператора
            if number:
                num = float("".join(number))
                number = []
                numbers.append(num)
            operations.append(expression[index[0]])
        index[0] += 1
       
    if number:#Тут еще может остаться неучтенное число
        num = float("".join(number))
        number = []
        numbers.append(num)

    i = 0
    while i < len(operations):
        if operations[i] == '*':
            numbers[i] *= numbers[i+1]
            numbers.pop(i+1)
            operations.pop(i)
        elif operations[i] == '/':
            numbers[i] /= numbers[i+1]
            numbers.pop(i+1)
            operations.pop(i)
        else:
            i += 1

    i = 0
    while i < len(operations):
        if operations[i] == '+':
            numbers[i] += numbers[i+1]
            numbers.pop(i+1)
            operations.pop(i)
        elif operations[i] == '-':
            numbers[i] -= numbers[i+1]
            numbers.pop(i+1)
            operations.pop(i)
        else:
            i += 1
    return numbers[0]

#Основное тело программы

input_string = input('Введите арифметическое выражение для вычисления, например 1+1 (без знака = ) ')
expression = list(input_string)

print('Ответ: ', calc(expression))

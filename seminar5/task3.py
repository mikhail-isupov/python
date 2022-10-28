# Игра в крестики-нолики

import random as rnd

def show_field(field, size):
#Печать игрового поля
    print()
    for j in range(size):
        print('   ', j, end ='')

    for i in range(size):
        print()
        print(i, end='')
        for j in range(size):
            if field[i][j]:
                print('  x  ' if field[i][j] == 1 else '  o  ', end ='')
            else:
                print('  .   ', end='')
    print()
            
def you_set_field(field,  size):
#Пользователь вводит номер поля
    while True:
        print('Введите через пробел номер ряда и столбца для поля, где хотите поставить крестик. Например, 0 0')
        choise = input()
        i, j = map(int, choise.split())
        if size > i >= 0 and size > j >= 0 and not field[i][j]:
            field[i][j] = 1
            break
        elif not (size > i >= 0 and size > j >= 0):
            print('Некорректные значения координат поля')
        else:
            print('Поле занято.')

    print()
    
def calculate_coords(line_number, pos_in_line, size):
#Пересчет от номера линии игрового поля и позиции пустого поля на этой линии к координатам игрового поля    
    if line_number < size:
        return [line_number, pos_in_line]
    elif 2 * size > line_number >= size:
        return [pos_in_line, line_number - size]
    elif line_number == 2 * size:
        return [pos_in_line, pos_in_line]
    else:
        return [size - 1 - pos_in_line, pos_in_line]

def get_column(field, index):
#Выделение данных в нужной колонке игрового поля
    column = []
    for i in range(len(field)):
        column.append(field[i][index])
    return column
        
def bot_set_field(field, size):
#Бот делает ход
    print()
    print('Ходит бот')

    i =  size  // 2

    if not field[i][i]:
        field[i][i] = -1
        return
    
    lines = []
    for i in range(size):
        lines.append(field[i]) 
    for i in range(size):
        lines.append(get_column(field, i))
    lines.append([field[i][i] for i in range(size)])
    lines.append([field[-1-i][i] for i in range(size)])

    min_sum = max_sum = min_index = max_index = None

    for i in range(len(lines)):
        if 0 in lines[i] and 1 not in lines[i]:
            min_sum = max_sum = sum(lines[i])
            min_index = max_index = i
            break
    
    if min_sum == None:
        for i in range(len(lines)):
            if 0 in lines[i]:
                min_sum = max_sum = sum(lines[i])
                min_index = max_index = i
                break
        
    for i in range(len(lines)):
       if 0 in lines[i]:
            if sum(lines[i]) < min_sum and 1 not in lines[i]:
               min_sum = sum(lines[i])
               min_index = i
            elif sum(lines[i]) > max_sum:
               max_sum = sum(lines[i])
               max_index = i

    if min_sum == 1 - size:
        coords = calculate_coords(min_index, lines[min_index].index(0), size)   
    elif max_sum == size - 1:
        coords = calculate_coords(max_index, lines[max_index].index(0), size)
    else:
        coords = calculate_coords(min_index, lines[min_index].index(0), size)

    field[coords[0]][coords[1]] = -1

def check_if_win(field, size):

    diagonal1 = diagonal2 = 0
    
    for i in range(size):
        row = sum(field[i])
        column = sum(get_column(field, i))
        diagonal1 += field[i][i]
        diagonal2 += field[-1 - i][i]
        if abs(row) == size or abs(column) == size:
            return True
    if abs(diagonal1) == size or abs(diagonal2) == size:
        return True

    return False
    

def check_if_draw(field, size):

    for i in range(size):
            if 0 in field[i]:
                return False
    return True
    

print('Игра Крестики-нолики')
print()
print('Для того, чтобы поставить  знак в нужной клетке,  необходимо ввести номер ее ряда и колонки. ')
print()
print('Вы ходите крестиком. Бот ходит ноликом. Кто начинает первым - определяет псевдослучайность. ')
print()

field_size = 3

field = [[0]*field_size for i in range(field_size)]

player_is_you = rnd.randint(0, 1)

show_field(field, field_size)

win = draw = False

while not (win or draw):

    player_is_you = abs(player_is_you - 1)
    
    if player_is_you:
        you_set_field(field, field_size)
    else:
        bot_set_field(field, field_size)

    show_field(field, field_size)

    win = check_if_win(field, field_size)

    draw = check_if_draw(field, field_size)

if win:
    print('Победа ', 'Ваша.' if player_is_you else 'бота.')
else:
    print('Ничья')
    

    
        
        
    







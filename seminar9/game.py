# Игра в крестики-нолики
import sys
import random as rnd
import tkinter as tk

class Game:
    def __init__(self, field_size=3):
#Инициализируется игровое поле, навешиваются обработчики событий.
        self.field = [[0]*field_size for i in range(field_size)]
        self.buttons = [[None] * field_size for i in range(field_size)]
        self.size = field_size
        self.window = tk.Tk()
        self.window.title('Крестики-нолики')
        for i in range(field_size):
            for j in range(field_size):
                self.buttons[i][j] = tk.Button(self.window, text='', height=3, width=3, command = lambda x=i, y=j: self.click_handler(x,y))
                self.buttons[i][j].grid(row=i, column=j)
        bot_first = rnd.randint(0, 1)
        if bot_first:
            self.bot_move()
        self.window.mainloop()
    
    def check_if_draw(self):
    #Проверка на ничью (Все поля заняты)
        for i in range(self.size):
                if 0 in self.field[i]:
                    return False
        return True

    def get_column(self, index):
    #Выделение данных в нужной колонке игрового поля
        column = []
        for i in range(self.size):
            column.append(self.field[i][index])
        return column

    def check_if_win(self):
    #Проверка на победу.
        diagonal1 = diagonal2 = 0 
        for i in range(self.size):
            row = sum(self.field[i])
            column = sum(self.get_column(i))
            diagonal1 += self.field[i][i]
            diagonal2 += self.field[-1 - i][i]
            if abs(row) == self.size or abs(column) == self.size:
                return True
        if abs(diagonal1) == self.size or abs(diagonal2) == self.size:
            return True
        return False

    def calculate_coords(self, line_number, pos_in_line):
    #Пересчет от номера линии игрового поля и позиции пустого поля на этой линии к координатам игрового поля    
        if line_number < self.size:
            return [line_number, pos_in_line]
        elif 2 * self.size > line_number >= self.size:
            return [pos_in_line, line_number - self.size]
        elif line_number == 2 * self.size:
            return [pos_in_line, pos_in_line]
        else:
            return [self.size - 1 - pos_in_line, pos_in_line]

    def bot_move(self):
    #Бот делает ход
        
        i =  self.size // 2
        if not self.field[i][i]:
            self.field[i][i] = -1
            self.buttons[i][i]['text'] = 'O'
            return
        
        lines = []
        for i in range(self.size):
            lines.append(self.field[i]) 
        for i in range(self.size):
            lines.append(self.get_column(i))
        lines.append([self.field[i][i] for i in range(self.size)])
        lines.append([self.field[-1-i][i] for i in range(self.size)])

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

        if min_sum == 1 - self.size:
            coords = self.calculate_coords(min_index, lines[min_index].index(0))   
        elif max_sum == self.size - 1:
            coords = self.calculate_coords(max_index, lines[max_index].index(0))
        else:
            coords = self.calculate_coords(min_index, lines[min_index].index(0))

        self.field[coords[0]][coords[1]] = -1
        self.buttons[coords[0]][coords[1]]['text'] = 'O'
        if self.check_if_win():
            print('Победил бот.')
            sys.exit()
        elif self.check_if_draw():
            print('Ничья.')
            sys.exit()  

    def click_handler(self, i, j):
    #Пользователь кликает по ячейке игрового поля, и если она не занята, то
        if not self.field[i][j]:
            self.field[i][j] = 1
            self.buttons[i][j]['text'] = 'X'
            if self.check_if_win():
                print('Вы победили.')
                sys.exit()
            elif self.check_if_draw():
                print('Ничья.')
                sys.exit()
            else:
                self.bot_move()

if __name__ == "__main__":
    print('Игра Крестики-нолики')
    print()
    print('Вы ходите крестиком. Бот ходит ноликом. Кто начинает первым - определяет псевдослучайность. ')
    print()
    field_size = int(input('Введите размер игрового поля: '))
    game = Game(field_size)
    

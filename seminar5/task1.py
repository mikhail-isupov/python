#Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

input_name = input('Введите имя входного файла: ')

output_name = input('Введите имя выходного файла: ')

stop_symbols = {'а', 'б', 'в'}

with open(input_name, encoding = "utf-8") as input_file:
# Без указания кодировки из файла читалась абракадабра
    with open(output_name, 'w') as output_file:
        for line in input_file:
            filtered_words = list(filter(lambda s: not stop_symbols <= set(s.lower()), line.split()))
            output_line = " ".join(filtered_words)
            output_file.write(output_line + "\n")


    
        


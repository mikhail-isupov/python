#Описание структуры данных и методов работы с ними
class Database:
    def __init__(self, header=None, file_name=None):
        self.data = {} #Данные в памяти будут храниться в виде словаря списков {id:[record]}
        self.separator = chr(0) #Символ-разделитель для разделения полей записи в файле
        self.skip = '-' #Символ для пустого или пропущенного поля записи
        self.rel_char = '@' #Символ для обозначения связанного поля
        self.related_dataset = False #Флаг для обозначения наличия связанных данных  
        #Новый объект данных может быть создан либо инициализацией списком полей в записи header,
        #Либо загрузкой файла из файла file_name, либо по умолчанию создается телефонный справочник
        if file_name:
            with open(file_name, encoding='utf-8') as file:
                header = file.readline().rstrip()
                if self.rel_char in header:
                    self.related_dataset = True
                self.record_fields = header.split(self.separator)     
                for line in file:
                    data = line.rstrip().split(self.separator)
                    if len(data) == len(self.record_fields) +1:
                        record_id = data[0]
                        self.update(record_id, data[1:])
        elif header:
            if self.rel_char in header:
                self.related_dataset = True
            self.record_fields = header.split()
            #separator используется для работы с файлами,
            #Пользователь разделяет поля пробелами.
        else:
            self.record_fields = ['Имя', 'Фамилия', 'Место_Работы', 'Контакты']

        
        #Название поля может быть как обычным, например, 'Имя', либо быть названием связанной таблицы
        #В этом случае имя поля должно начинаться с @ и содержать ссылку на связанную таблицу, например @file_name.csv
        #А данные в поле должны быть соотвествующими id связанной таблицы
        #Этот вариант программы написан для простейшего случая когда связанная таблица содержит лишь id и одну колонку c данными

    def update(self, record_id, record):
    #Создание новой записи в базе если record_id нет, либо перезапись существующей. 
    #Данные передаются в виде списка record
        if record_id in self.data:
            for i in range(len(record)):
                if record[i] != self.skip:
                    self.data[record_id][i] = record[i] #Перезаписываются только измененные поля
        else:
            self.data[record_id] = record
    
    def delete(self, record_id):
    #Удаление записи по id
        return self.data.pop(record_id, False)

    def save(self, file_name):
        with open(file_name, mode='w', encoding='utf-8') as file:
            #Запись заголовка со структурой данных
            header = self.separator.join(self.record_fields) + '\n'
            file.write(header)
            for record_id in self.data: 
                #Запись данных
                output_string = record_id + self.separator + self.separator.join(self.data[record_id]) + '\n'
                file.write(output_string)
    
    def find(self, field, value): #Поиск в поле field значения value
        index = None
        for i in range(len(self.record_fields)): #Для поиска по имени поля его индекса
            if self.record_fields[i].lower() == field.lower():
                index = i
                break
        if index is None:
            return False
        
        #Формируется и возвращается новый объект Database, в котором находятся записи с полем field содержащим value
        db_header = ' '.join(self.record_fields)
        filter_db = Database(header=db_header)
        for record_id in self.data:
            if value.lower() in self.data[record_id][index].lower():
                filter_db.update(record_id, self.data[record_id])
        return filter_db

    def merge(self):
    #текущий объект изменяется, данные из связанных таблиц вытаскиваются и встраиваются в таблицу.
    #Этот вариант программы написан для простейшего случая когда связанная таблица содержит лишь id и одну колонку c данными
    #Что сильно упрощает слияние таблиц
        
        if not self.related_dataset:
            return False #Нет связанных таблиц
        
        for i in range(len(self.record_fields)):
            if self.rel_char in self.record_fields[i]:
                filename = self.record_fields[i][1:] #Отбрасывается символ и получаем имя связанной таблицы
                linked_table = Database(file_name = filename) #Из файла подгружается связанная таблица
                self.record_fields[i] = linked_table.record_fields[0] #Меняется название колонки на название колонки из связанной таблицы
                for record_id in self.data:
                    linked_id = self.data[record_id][i] #В соответствующем поле записан id связанной таблицы
                    if linked_id in linked_table.data:
                        self.data[record_id][i] = linked_table.data[linked_id][0] #Колонка в связанной таблице всего одна

        return True
                
                
                


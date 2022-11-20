#Описание структуры данных и методов работы с ними
class Phonebase:
    def __init__(self):
        self.record_fields = ('Имя', 'Фамилия', 'Дата_Рождения', 'Место_Работы', 'Контакты')
        #Задает исходный набор и последовательность полей в записи. 
        self.data = {}
        #Данные будут храниться в виде словаря списков {id:[record]}
        self.separator = chr(0) #Симол-разделитель
        self.skip = '-' #Символ для пустого или пропущенного поля

    def update(self, id, record):
    #Создание новой записи в телефонном справочнике если id нет, либо перезапись существующей. 
    #Данные передаются в виде списка record
        if id in self.data:
            for i in range(len(record)):
                if record[i] != self.skip:
                    self.data[id][i] = record[i] #Перезаписываются только измененные поля
        else:
            self.data[id] = record
    
    def delete(self, id):
    #Удаление записи по id
        return self.data.pop(id, False)

    def save(self, file_name):
        with open(file_name, mode='w', encoding='utf-8') as file:
            #Запись заголовка со структурой данных
            header = self.separator.join(self.record_fields) + '\n'
            file.write(header)
            for id in self.data: #Запись данных
                output_string = id + self.separator + self.separator.join(self.data[id]) + '\n'
                file.write(output_string)
    
    def load(self, file_name):    
        self.data = {}
        with open(file_name, encoding='utf-8') as file:
            header = file.readline()
            self.record_fields = header.split(self.separator)     
            for line in file:
                data = line.split(self.separator)
                if len(data) == len(self.record_fields) +1:
                    id = data[0]
                    self.update(id, data[1:])
    
    def find(self, field, value): #Поиск в поле field значения value
        index = None
        result = {} #Формируется словарь записей удовлетворяющих условию - в поле field есть value
        for i in range(len(self.record_fields)): #Для поиска по имени поля его индекса
            if self.record_fields[i].lower() == field.lower():
                index = i
                break
        
        if index is not None:
            for id in self.data:
                if value.lower() in self.data[id][i].lower():
                    result[id] = self.data[id]
        return result
                 


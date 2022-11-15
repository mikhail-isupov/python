#Модуль для вывода сообщений телефонного справочника
def message(msg): #вывод однострочного сообщения
    print(msg)

def view_data(data): #Просмотр данных справочника
    for id in sorted(data):
        output_string = id + ' ' + ' '.join(data[id])
        print(output_string)

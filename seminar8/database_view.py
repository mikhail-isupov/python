#Модуль для вывода сообщений базы данных
from database import Database
def message(msg): #вывод однострочного сообщения
    print(msg)

def view_data(db): #Просмотр данных справочника
    header = ['id'] + db.record_fields
    format_string = "{:15} "*len(header)
    print(format_string.format(*header))
    
    for record_id in sorted(db.data):
        output = list(record_id) + db.data[record_id]
        print(format_string.format(*output))

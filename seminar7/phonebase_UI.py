# Модуль организует взаимодействие между модулем для организации и работы с данными phonebase, 
# модулем вывода результата phonebase_view, модулем логирования phonebase_log и пользователем
from phonebase import Phonebase
import phonebase_view as view
from phonebase_log import log 

def get_user_data():
    data = ''
    while not data:
        data = input()   
    return data

def show_phonebase(phonebook):
    header = 'id ' + ' '.join(phonebook.record_fields) #Вывод структуры справочника
    view.message(header)
    view.view_data(phonebook.data)

def update_phonebase(phonebook):
    view.message('Каждая запись в справочнике имеет свой уникальный id (например, порядковый номер записи).')
    view.message('Введите id записи. Если id в справочнике нет, то создается новая запись, если уже есть - перезаписывается существующая.')
    id = get_user_data()
    data = []
    for i in range(len(phonebook.record_fields)):
        view.message('Введите значения поля ' + phonebook.record_fields[i])
        view.message('Если не хотите заполнять или редактировать это поле, введите ' + phonebook.skip)
        data.append(get_user_data())
    phonebook.update(id, data)
    log('Добавлена новая запись с id ' + id)

def delete_record(phonebook):
    view.message('Введите id записи,которую нужно удалить.')
    id = get_user_data()
    if phonebook.delete(id):
        log('Удалена запись справочника c id ' + id)
    else:
        view.message('Ошибка! Такого id в справочнике нет.')

def find_record(phonebook):
    view.message('Введите название поля записи, в котором нужно будет искать (например, по фамилии): ')
    field = get_user_data()
    view.message('Введите текст,который ищете.')
    value = get_user_data()
    view.view_data(phonebook.find(field, value))

def load_phonebase(phonebook):
    view.message('Введите название файла с данными для загрузки.')
    file_name = get_user_data()
    phonebook.load(file_name)

def save_phonebase(phonebook):
    view.message('Введите название файла, куда будут сохранены данные.')
    file_name = get_user_data()
    phonebook.save(file_name)

def run():
    phonebook = Phonebase() #Создание справочника
    while True:
        view.message('Телефонный справочник. Выберите действия:')
        view.message('1: Просмотреть содержимое справочника.')
        view.message('2: Добавить новую запись или перезаписать имеющуюся.')
        view.message('3: Удалить запись.')
        view.message('4: Найти нужные записи.')
        view.message('5: Экспортировать содержимое справочника в файл.')
        view.message('6: Импортировать содержимое справочника из файла.')
        view.message('7: Выход из справочника.')
        
        option = get_user_data()

        if option == '1':
            show_phonebase(phonebook)
        elif option == '2':
            update_phonebase(phonebook)
        elif option == '3':
            delete_record(phonebook)
        elif option == '4':
            find_record(phonebook)
        elif option == '5':
            save_phonebase(phonebook)
        elif option == '6':
            load_phonebase(phonebook)
        elif option == '7':
            break
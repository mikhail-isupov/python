# Модуль организует взаимодействие между модулем для организации и работы с данными database, 
# модулем вывода результата database_view, модулем логирования database_log и пользователем
from database import Database
import database_view as view
from database_log import log 

def get_user_data():
    data = ''
    while not data:
        data = input()   
    return data

def main_menu():
        view.message('Работа с базами данных. Выберите действия:')
        view.message('1: Создать новую базу данных.')
        view.message('2: Загрузить существующую.')
        view.message('3: Просмотреть содержимое базы данных.')
        view.message('4: Редактировать существующую запись или добавить новую.')
        view.message('5: Удалить запись из базы данных.')
        view.message('6: Найти нужные записи в базе данных.')
        view.message('7: Объединить связанные таблицы.')
        view.message('8: Сохранить данные.')
        view.message('9: Выход.')

def create_new_db():
    view.message('Введите через пробел список полей в записи базы данных, например: Фамилия Имя Отчество ДР Контакты')
    view.message('Колонку id указывать не нужно - она добавляется автоматически')
    view.message('Если хотите связать текущую таблицу с другой таблицей, добавьте имя связанной таблицы в название поля с символом @')
    view.message('Например: Фамилия Имя Отчество @position.csv')
    view.message('Текущая версия работает со связанными таблицами, содержащими только одну колонку данных')
    db_header = get_user_data()
    result = Database(header=db_header)
    log('Создана новая база данных')
    return result

def load_db():
    view.message('Введите название файла с данными для загрузки.')
    filename = get_user_data()
    result = Database(file_name=filename)
    return result

def update_db(db):
    view.message('Каждая запись в справочнике имеет свой уникальный id (например, порядковый номер записи).')
    view.message('Введите id записи. Если id в справочнике нет, то создается новая запись, если уже есть - перезаписывается существующая.')
    record_id = get_user_data()
    data = []
    for i in range(len(db.record_fields)):
        view.message('Введите значения поля ' + db.record_fields[i])
        view.message('Если не хотите заполнять или редактировать это поле, введите ' + db.skip)
        data.append(get_user_data())
    db.update(record_id, data)
    log('Добавлена новая запись с id ' + record_id)

def delete_record(db):
    view.message('Введите id записи,которую нужно удалить.')
    record_id = get_user_data()
    if db.delete(record_id):
        log('Удалена запись справочника c id ' + record_id)
    else:
        view.message('Ошибка! Такого id в справочнике нет.')

def find_record(db):
    view.message('Введите название поля записи, в котором нужно будет искать (например, по фамилии): ')
    field = get_user_data()
    view.message('Введите текст,который ищете.')
    value = get_user_data()
    result = db.find(field, value)
    if result:
        view.view_data(result)
    else:
        view.message('Такого поля в записи нет')

def db_merge(db):
    if db.merge():
        log('Объединены связанные таблицы')
    else:
        view.message('В базе нет ссылок на связанные таблицы.')

def save_db(db):
    view.message('Введите название файла, куда будут сохранены данные.')
    file_name = get_user_data()
    db.save(file_name)
    log('База данных сохранена')

def run():

    db = Database()
    
    while True:

        main_menu()
        
        option = get_user_data()

        if option == '1':
            db = create_new_db()
        elif option == '2':
            db = load_db()
        elif option == '3':
            view.view_data(db)
        elif option == '4':
            update_db(db)
        elif option == '5':
            delete_record(db)
        elif option == '6':
            find_record(db)
        elif option == '7':
            db_merge(db)
        elif option == '8':
            save_db(db)
        elif option == '9':
            break
            

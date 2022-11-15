#Логирование данных
from datetime import datetime
def log(record):
    with open('log.txt', 'a') as file:
        output_string = str(datetime.now()) + ' ' + record + '\n'
        file.write(output_string)
    
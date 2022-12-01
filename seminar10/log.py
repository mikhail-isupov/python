from telegram import Update
from datetime import datetime
def log(update: Update, result=''):
    dt = str(datetime.now())
    if result:
        output_string = ' '.join([dt, str(update.effective_user), result]) + '\n'
    else:
        output_string = ' '.join([dt, str(update.effective_user), update.message.text]) + '\n'
    with open('log.txt', mode='a') as file:
        file.write(output_string)
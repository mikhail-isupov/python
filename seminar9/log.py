from telegram import Update
from datetime import datetime
def log(update: Update, result):
    dt = str(datetime.now())
    output_string = ' '.join([dt, str(update.effective_user), update.message.text, result, '\n'])
    with open('log.txt', mode='a') as file:
        file.write(output_string)
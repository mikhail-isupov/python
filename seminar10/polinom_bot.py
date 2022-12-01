#Суммирование полиномов
#Сделан на основе эхобота
#https://github.com/python-telegram-bot/python-telegram-bot/blob/v13.x_api6.3/examples/echobot.py

import polinom
from log import log

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# Define a few command handlers. These usually take the two arguments update and
# context.
class PolinomHandler:
    def __init__(self):
        self.vectors = [] #Введенные пользователем данные

    def polinom_handler(self, update: Update, context: CallbackContext):
        log(update)
        vector = polinom.convert(update.message.text)
        if vector:
            self.vectors.append(vector)
            if len(self.vectors) == 1:
                update.message.reply_text('Введите второй полином.')
            else:
                result = polinom.sum(self.vectors[0], self.vectors[1])
                self.vectors = []
                reply = 'Результат: ' + polinom.convert(result)
                log(update, reply)
                update.message.reply_text(reply)
                update.message.reply_text('Введите первый полином.')
        else:
            reply = 'Бот не смог понять сообщение, повторите.'
            log(update, reply)
            update.message.reply_text(reply)

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Привет, {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )
    start_message ='''Этот бот умеет складывать полиномы разных степеней. Для справки введите команду /help
    Или пришлите полином.'''
    update.message.reply_text(start_message)
    
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    help_message = '''Полиномы можно записывать по разному. Например, так: x^2-2x+1 
    Или так: x**2-2*x+1. Или так: x2-2x+1. Можно и так: 1-2x+x2. Присылайте, как вам удобнее.'''
    update.message.reply_text(help_message)

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("TOKEN")
    message = PolinomHandler() #Объект содержащий обработчик сообщений и введенные данные

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Вызов калькулятора полиномов
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message.polinom_handler))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
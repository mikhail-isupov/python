#Калькулятор арифметических выражений (ARithmetic EXPressions CALCulator)
#Сделан на основе эхобота
#https://github.com/python-telegram-bot/python-telegram-bot/blob/v13.x_api6.3/examples/echobot.py

from calc import calc
from log import log

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Привет, {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )
    update.message.reply_text('Этот бот умеет вычислять арифметические выражения со всякими скобочками.')
    update.message.reply_text('Просто введите арифметическое выражение или команду /help для помощи.')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Введите арифметическое выражение для вычисления, например: (1+1)/(-1-1)*-1')


def arexpcalc(update: Update, context: CallbackContext) -> None:
    #Вычисление введенного выражения и ответ
    expression = list(update.message.text)
    result = str(calc(expression))
    update.message.reply_text(result)
    log(update, result)

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("TOKEN")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Вызов калькулятора
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, arexpcalc))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
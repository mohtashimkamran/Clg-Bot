from telegram import Update
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,CallbackContext
from telegram import Bot,ReplyKeyboardMarkup,Update
import text


def start(update:Update,context:CallbackContext):
    author = update.message.from_user.first_name
    reply = "Hello "+"{}".format(author)+"!"
    update.message.reply_text(reply + text.welcome_text)

def help(update:Update,context:CallbackContext):
    author = update.message.from_user.first_name
    reply = "Hello "+"{}".format(author)+" This is an Information bot!"
    update.message.reply_text(reply)





def main():
    updater = Updater("5089790707:AAHytQvl34MDIXsyo1Ne5PldiwcR7PNvhnk", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start',start))
    dispatcher.add_handler(CommandHandler('help',help))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
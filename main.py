from config import Config
from bot import start,help,dl
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    """Start the bot."""
    updater = Updater(Config.token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))


    # on noncommand i.e message - echo the message on Telegra
    dp.add_handler(MessageHandler(Filters.text, dl))
    #dp.add_handler(MessageHandler(Filters.text, echo))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
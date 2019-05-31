

from telegram.ext import Updater # pip install python-telegram-bot --upgrade

updater = Updater(token='897931472:AAGCPoNSM_Et2G3JFxadCdwj6YSO67UB_tM')#, use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

import telebot

from telebot import apihelper
# apihelper.proxy = {'http':'http://10.10.1.10:3128'}
apihelper.proxy = {'https':'socks5h://userproxy:password@212.129.45.147:30509'}

bot = telebot.TeleBot("897931472:AAGCPoNSM_Et2G3JFxadCdwj6YSO67UB_tM")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, let's start working")

# повтор ботом сообщения (или же ответ на сообщение)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling(none_stop=True)
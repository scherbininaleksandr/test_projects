
import telebot
bot = telebot.TeleBot("897931472:AAGCPoNSM_Et2G3JFxadCdwj6YSO67UB_t")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
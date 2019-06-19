# pip install: virtualenv

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
from bot_1_token import TOKEN, TOKEN_Dialogflow

# proxy socks5
# TOKEN =
# TOKEN_Dialogflow =
# CHAT_ID = '342423423523'
REQUEST_KWARGS = {
    'proxy_url': 'socks5://192.169.197.146:49694'
    # Optional, if you need authentication:
    # 'urllib3_proxy_kwargs': {
    #    'username': 'telebot',
    #    'password': 'ksdafjlk3wart',
    # }
}

updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)  # Токен API к Telegram
dispatcher = updater.dispatcher


# Обработка команд
def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Привет, let's talk?")


def textMessage(bot, update):
    request = apiai.ApiAI(TOKEN_Dialogflow).text_request()  # Токен API к Dialogflow
    request.lang = 'ru'  # На каком языке будет послан запрос
    request.session_id = 'onetestonebot'  # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = update.message.text  # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')


#отправка файлов в чат телеграм
def sendScreenshot(bot, update):
   photo = open("C:/Users/nikolskiy-d/Desktop/screenshots/1.jpg", 'rb')
   bot.send_photo(chat_id, photo)             # or chat_id = update.message.chat_id
   bot.send_photo(chat_id, "FILEID")


# Хендлеры (присваивание уведомлениям команды обработки и начать поиск обновления команд)
send_screenshot_handler = CommandHandler('screen', sendScreenshot)
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
# Добавляем хендлеры в диспетчер
dispatcher.add_handler(send_screenshot_handler)
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
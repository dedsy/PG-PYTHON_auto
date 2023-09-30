import telebot
from config import token
from work_with_excel import search_excel


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Введите имя сотрудника, данные которого хотите получить.")


@bot.message_handler(content_types=['text'])
def handle_message(message):
    result = search_excel(message.text)
    if result:
        for i in result:
            bot.send_message(message.chat.id, i)
    else:
        bot.send_message(message.chat.id, "По запросу ничего не найдено.")


bot.infinity_polling()

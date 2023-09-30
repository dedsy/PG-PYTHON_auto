import requests
import telebot
from config import token


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    # bot.send_message(message.chat.id,"Привет ✌️ ")
    bot.reply_to(message, "Привет ✌️ ")


# @bot.message_handler(content_types=('text', 'photo', 'sticker'))
# def handle_message(message):
#     if message.text

bot.infinity_polling()

import telebot
from telebot import types
from config import TOKEN, API
from main import get_weather

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    with open('statik/Sticker2.tgs', 'rb') as sti:
        bot.send_sticker(message.chat.id, sti)
    text = 'Im weathers BOT'
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':
        t = get_weather(message.text, API)
        bot.send_message(message.chat.id, t)


bot.polling(non_stop=True)

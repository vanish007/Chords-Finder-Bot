import os
from dotenv import load_dotenv
import telebot
from random import randint

load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_BOT']
bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)


@bot.message_handler(commands=['restart'])
def send_welcome(message):
    bot.reply_to(message, "Список команд:\n"
                          "/restart -обновить бота\n"
                          "/dice - случайное предсказание\n"
                          "/donate - поддержать автора деньгами\n"
                          "/song - найти аккорды для песни \n")

@bot.message_handler(commands=['song'])
def send_welcome(message):
    bot.reply_to(message, "https://google.com")

@bot.message_handler(commands=['dice'])
def send_welcome(message):
    num = randint(0, 1)
    wish = ["Сегодня вас ждет успех!", "Завтра вас собьет автобус"]
    bot.reply_to(message, wish[num])


@bot.message_handler(commands=['donate'])
def send_welcome(message):
    bot.reply_to(message, "+7-(921)-777-77-77")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()

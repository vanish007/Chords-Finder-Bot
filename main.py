import os
from dotenv import load_dotenv
import telebot
from random import randint

load_dotenv()

TELEGRAM_TOKEN = os.environ['TELEGRAM_BOT']
bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Список команд:\n"
						  "/start - список команд\n"
						  "/dice - случайное число от 1-6\n"
						  "/randint - случайное число из пользовательского диапозона\n"
						  "/donate - поддержать автора деньгами\n")

@bot.message_handler(commands=['dice'])
def send_welcome(message):
	num = randint(1, 6)
	bot.reply_to(message, str(num))

# @bot.message_handler(commands=['randint'])
# def send_welcome(message):
# 	bot.reply_to(message, "Введите нижнюю границу: ")
# 	low = int(input())
# 	bot.reply_to(message, "Введите верхнюю границу: ")
# 	high = int(input())
# 	while high < low:
# 		bot.reply_to(message, "Верхняя граница меньше нижней. \
# 		Бот присылает случайное число из диапозона от нижней границы до верхней включительно, \
# 		а поэтому верхняя граница должна быть больше нижней. Введите верхнюю границу еще раз: ")
# 		high = int(input())
# 	num = randint(low, high)
# 	bot.reply_to(message, str(num))

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
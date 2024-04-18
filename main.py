from aiogram import Bot, Dispatcher, executor
from os import environ
from dotenv import load_dotenv
from random import randint


load_dotenv()
TOKEN = environ['TOKEN']
bot = Bot(TOKEN)
dp = Dispatcher(bot)


class text:
    help_command_text = """
/помощь - список команд
/старт - начать работу с ботом
/описание - описание бота
"""
    start_command_text = """
Введите название песни в формате "АВТОР - НАЗВАНИЕ ПЕСНИ".
Например: Кино - Звезда по имени солнце.'
"""
    description_command_text = """
Бот для сохрание ваших любимых песен в удобном формате
"""


count = 0


@dp.message_handler(commands=['описание'])
async def description(message):
    await message.reply(text.description_command_text)

@dp.message_handler(commands=['помощь'])
async def help(message):
    await message.reply(text.help_command_text)

@dp.message_handler(commands=['старт'])
async def start(message):
    await message.answer(text.start_command_text)

@dp.message_handler()
async def empty(message):
    global count
    if count == 0:
        await message.answer('Вы ввели неправильную команду...')
    elif count == 1:
        await message.answer('Вы снова ввели неправильную команду...')
    elif (count % 10 == 2 or count % 10 == 3 or count % 10 == 4) and count != 12 and count != 13 and count != 14:
        if count >= 10:
            t = (count // 10) * 10
            await message.answer(f'Вы ввели неправильную команду уже {t} раз... Возможно вам стоит заняться чем-то более полезным.')
        else:
            await message.answer(f'Вы ввели неправильную команду {count} раза...')
    else:
        if count >=  10:
            t = (count // 10) * 10
            await message.answer(f'Вы ввели неправильную команду уже {t} раз... Возможно вам стоит заняться чем-то более полезным.')
        else:
            await message.answer(f'Вы ввели неправильную команду {count} раз...')
    count += 1

if __name__ == '__main__':
    executor.start_polling(dp)
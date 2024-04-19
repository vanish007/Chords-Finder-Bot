from aiogram import Bot, Dispatcher, executor
from aiogram.types import *
from os import environ
from dotenv import load_dotenv
from aiogram.dispatcher.filters import Text
from time import sleep


load_dotenv()
TOKEN = environ['TOKEN']
bot = Bot(TOKEN)
dp = Dispatcher(bot)


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


class text:
    help_command_text = """
<b>/help</b> - список команд
<b>/start</b> - начать работу с ботом
<b>/description</b> - описание бота
<b>/location</b> - отправить текущую локацию
<b>/dice</b> - кинуть кубик
<b>/links</b> - полезные ссылки
"""
    start_command_text = """
Введите название песни в формате "АВТОР - НАЗВАНИЕ ПЕСНИ".
Например: <em>Кино - Звезда по имени солнце.</em>'
"""
    description_command_text = """
Бот для сохрание ваших любимых песен в удобном формате
"""


count = 0


kb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
kb1 = KeyboardButton('/help')
kb2 = KeyboardButton('/links')
kb.add(kb1).insert(kb2)
ikb = InlineKeyboardMarkup()
ikb1 = InlineKeyboardButton(text='Конспект',
                            url='https://bakasa.notion.site/Python-201-2022-2024-34a5d5401c964396864f1739592352fd')
ikb2 = InlineKeyboardButton(text='GitHub',
                            url='https://github.com/aip-python-pro-2023')
ikb.add(ikb1, ikb2)
nbp = InlineKeyboardMarkup()
nbp1 = InlineKeyboardButton(text='.pdf',
                           callback_data='11')
nbp2 = InlineKeyboardButton(text='.txt',
                           callback_data='12')
nbp.add(nbp1, nbp2)
ptxt = """
　 Em 　 　Am 　　 　　 　C　　 　 D 　　　Em
Я сижу и смотрю в чужое небо из чужого окна
　　Am　　　　C　　　D　　　　Em
И не вижу ни одной знакомой звезды.
　　Am　　　　　 C　　　D　　　　Em
Я ходил по всем дорогам и туда, и сюда,
　　Am　　　　 　 C　　　　 D　　　Em
Обернулся - и не смог разглядеть следы.


Припев:

　　 　Am　　　　　　C　　D　　Em
Но если есть в кармане пачка сигарет,

　　 　Am　　　　　　C　　　　D　　　　　Em
Значит все не так уж плохо на сегодняшний день.

　　 Am　　　　C　　　　　D　　　　Em
И билет на самолет с серебристым крылом,

　　 　Am　　　　C　　　　D　　　Em
Что, взлетая, оставляет земле лишь тень.

2 Куплет

И никто не хотел быть виноватым без вина,
И никто не хотел руками жар загребать,
А без музыки на миру смерть не красна,
А без музыки не хочется пропадать.
"""
zbp = InlineKeyboardMarkup()
zbp1 = InlineKeyboardButton(text='.pdf',
                           callback_data='21')
zbp2 = InlineKeyboardButton(text='.txt',
                           callback_data='22')
zbp.add(zbp1, zbp2)
ztxt = """
　 　 　Am(4)
Белый снег, серый лед,
　　　　C(4)
На растрескавшейся земле.
　Dm(4)
Одеялом лоскутным на ней -
G(4)
Город в дорожной петле.
　　　Am(4)
А над городом плывут облака,
　　C(4)
Закрывая небесный свет.
　　　 Dm(4)
А над городом - желтый дым,
G(4)
Городу две тысячи лет,
　Dm(4)
Прожитых под светом Звезды
　　　　Am (4)
По имени Солнце...

И две тысячи лет - война,
Война без особых причин.
Война - дело молодых,
Лекарство против морщин.
Красная, красная кровь -
Через час уже просто земля,
Через два на ней цветы и трава,
Через три она снова жива
И согрета лучами Звезды
По имени Солнце...

И мы знаем, что так было всегда,
Что судьбою больше любим,
Кто живет по законам другим
И кому умирать молодым.
Он не помнит слово "да" и слово "нет",
Он не помнит ни чинов, ни имен.
И способен дотянуться до звезд,
Не считая, что это сон,
И упасть, опаленным Звездой
По имени Солнце...
"""
rbp = InlineKeyboardMarkup()
rbp1 = InlineKeyboardButton(text='.pdf',
                           callback_data='31')
rbp2 = InlineKeyboardButton(text='.txt',
                           callback_data='32')
rbp.add(rbp1, rbp2)
sbp = InlineKeyboardMarkup()
sbp1 = InlineKeyboardButton(text='.pdf',
                           callback_data='41')
sbp2 = InlineKeyboardButton(text='.txt',
                           callback_data='42')
sbp.add(sbp1, sbp2)
async def on_startup(_):
    print(color.YELLOW + color.BOLD + 'Бот был запущен!' + color.END)


@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgIAAxkBAAEL8bJmISjQsNIbrvwpA0XGgfiundcbYQACQhAAAjPFKUmQDtQRpypKgjQE')
    await message.answer(text.start_command_text,
                         parse_mode='HTML',
                         reply_markup=kb)


@dp.message_handler(commands=['help'])
async def help(message):
    await message.reply(text.help_command_text,
                        parse_mode='HTML')


@dp.message_handler(commands=['links'])
async def links(message):
    await message.answer(text='Ссылки',
                        reply_markup=ikb)


@dp.message_handler(commands=['description'])
async def description(message):
    await message.reply(text.description_command_text,
                        parse_mode='HTML')


@dp.message_handler(commands=['location'])
async def location(message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=59.956621,
                            longitude=30.310571)


@dp.message_handler(commands=['dice'])
async def dice(message):
    await bot.send_dice(chat_id=message.from_user.id)


@dp.message_handler(Text(equals='Кино - пачка сигарет'))
async def pachka1(message):
    await message.answer('Подождите, идет поиск...')
    sleep(1)
    await bot.send_message(chat_id=message.from_user.id,
                     text='Аккорды найдены. Выберите формат',
                     reply_markup=nbp)


@dp.message_handler(Text(equals='Полет шмеля'))
async def photo1(message):
    await message.answer('Подождите, идет поиск...')
    sleep(1)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Аккорды найдены. Выберите формат',
                           reply_markup=sbp)


@dp.message_handler(Text(equals='Ramstein - sonne'))
async def photo1(message):
    await message.answer('Подождите, идет поиск...')
    sleep(1)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Аккорды найдены. Выберите формат',
                           reply_markup=rbp)


@dp.message_handler(Text(equals='Кино - звезда по имени солнце'))
async def photo1(message):
    await message.answer('Подождите, идет поиск...')
    sleep(1)
    await bot.send_message(chat_id=message.from_user.id,
                           text='Аккорды найдены. Выберите формат',
                           reply_markup=zbp)


@dp.callback_query_handler()
async def queru(callback):
    if callback.data == '11':
        await bot.send_photo(chat_id =callback.message.chat.id,
                             photo=InputFile('Пачка.jpg'))
        await callback.answer()
    elif callback.data == '12':
        await callback.message.answer(ptxt)
        await callback.answer()
    elif callback.data == '21':
        await bot.send_photo(chat_id=callback.message.chat.id,
                             photo=InputFile('Звезда.jpg'))
        await callback.answer()
    elif callback.data == '22':
        await callback.message.answer(ztxt)
        await callback.answer()
    elif callback.data == '31':
        await bot.send_photo(chat_id=callback.message.chat.id,
                             photo=InputFile('Рамштейн.png'))
        await callback.answer()
    elif callback.data == '41':
        await bot.send_photo(chat_id=callback.message.chat.id,
                             photo=InputFile('Полёт.jpg'))
        await callback.answer()




@dp.message_handler()
async def empty(message):
    global count
    if count == 0:
        await message.answer('Вы ввели неправильную команду...')
    elif count == 1:
        await message.answer('Вы снова ввели неправильную команду...')
    elif count == 2 or count == 3 or count == 4:
        await message.answer(f'Вы ввели неправильную команду {count} раза...')
    elif count <= 8:
        await message.answer(f'Вы ввели неправильную команду уже {count} раз...'
                             f' Возможно вам стоит заняться чем-то более полезным.')
    elif count == 9:
        await bot.send_sticker(message.from_user.id,
                               sticker='CAACAgIAAxkBAAEL8cZmISloxUKV7jZqmMS8r94RWonulwACOhoAAknO8UldsQbBX-XwlTQE')
    elif count == 10:
        await bot.send_sticker(message.from_user.id,
                               sticker='CAACAgIAAxkBAAEL8c5mISmE7MEwzDFscb660eAgYifU2wACrBUAAvMKqUro9MnxJkxytjQE')
    elif count == 11:
        await bot.send_sticker(message.from_user.id,
                               sticker='CAACAgIAAxkBAAEL8dFmISmLENp-KrLDZ8cAAdsFf2TodsoAAs4ZAAKJEBBKhq0wFniF8sA0BA')
    elif count == 12:
        await bot.send_sticker(message.from_user.id,
                               sticker='CAACAgIAAxkBAAEL8dJmISmMWQiEiNvoXJy8LllQmV9bZQACeRYAAmgXEUqU9j6hEXb3kjQE')
    elif count == 13:
        await bot.send_sticker(message.from_user.id,
                               sticker='CAACAgIAAxkBAAEL8f1mIS0DYqos_QRvHM4FS3rEv8xLBQACJhUAAhY-IUsHeV052qwVRDQE')
    elif count == 14:
        await bot.send_sticker(message.from_user.id,
                               sticker='CAACAgIAAxkBAAEL8f9mIS0HizrXyvB4J71Of5x7sX7sxgAC_xcAAuARIEtG8X3ZtfBuuTQE')
    else:
        await message.answer(f'Количество неправильно введенных сообщений: {count}')
    count += 1


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
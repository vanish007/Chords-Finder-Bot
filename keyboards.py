from aiogram.types import *


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
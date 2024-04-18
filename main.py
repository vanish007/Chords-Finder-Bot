from aiogram import Bot, Dispatcher, executor
import os
import dotenv


dotenv.load_dotenv()
TOKEN = os.environ['TOKEN']
bot = Bot(TOKEN)
dp = Dispatcher(bot)





if __name__ == '__main__':
    executor.start_polling(dp)
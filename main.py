import config
import logging
import Task

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = config.token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Я гомогей")

bebr = Task.CalendarTask('задрилить', '14 12 1488')
print(bebr.get_info())

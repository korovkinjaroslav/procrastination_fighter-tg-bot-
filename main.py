import config
import logging
import Task
import asyncio

from aiogram import Bot, Dispatcher, types

API_TOKEN = config.token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message()
async def greet_message(message: types.Message):
    await message.answer(
        text="Я лишь робот. Лишь имитация жизни. Я не сочиню симфонию. Не превращу кусок холста в шедевр искусства.\n я хочу питсу",
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

asyncio.run(main())

bebr = Task.CalendarTask('задрилить', '11 9 1488')
print(bebr.get_info())

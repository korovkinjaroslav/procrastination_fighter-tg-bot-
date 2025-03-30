import config
import aiogram
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = config.token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Я лишь робот. Лишь имитация жизни. Я не сочиню симфонию. Не превращу кусок холста в шедевр искусства.\n я хочу питсу")


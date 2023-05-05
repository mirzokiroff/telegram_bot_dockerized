import os

from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import logging

from db import create_table, con

logging.basicConfig(level=logging.INFO)
load_dotenv('.env')
API_TOKEN = os.getenv('TOKEN')

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)
cur = con.cursor()


@dp.message_handler()
async def main_menu(message: types.Message):
    await message.answer(message.text)
    query = '''
    INSERT INTO history(user_id, msg) VALUES (%s, %s);
    '''
    cur.execute(query, (message.from_user.id, message.text))
    con.commit()


async def on_startup(dp):
    create_table()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

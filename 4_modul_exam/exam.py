# 1 task

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

TOKEN = "6108967749:AAH7aVD7nSyHk6FZjdOjLWdHbYiVFkS_6rU"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def process_message(message: types.Message):
    text = message.text

    unli_count = sum([1 for char in text if char.lower() in ['a', 'e', 'i', 'o', 'u']])

    if unli_count > 5:
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)











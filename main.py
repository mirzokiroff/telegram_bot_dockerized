import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
# from dotenv import load_dotenv

# load_dotenv('.env')
# BOT_TOKEN = os.getenv('TOKEN1')

# salomlashish = ['salom', 'salomalekom', 'assalomu alaykum', 'nma gap', "Assalomu Aleyko'm"]
# xayrlashish = ['xayr', 'bye bye', "sog' bo'ling"]

BOT_TOKEN = '5935641446:AAFYXxw4IuVwChnDElESEWazcm81nDINSBc'
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


def main_btn():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton('📒Contact', request_contact=True),
               KeyboardButton('📍Location', request_location=True),
               KeyboardButton('🤵‍Tuman Hokimi', request_hokim=True),
               KeyboardButton('nimadir', request_nimadir=True))
    return markup


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    await message.answer(f'Assalomu Alaykum {message.from_user.full_name}')
    await message.answer(text="Assalomu Alaykum, sizga kerak bo'lgan bo'limni tanlang", reply_markup=main_btn())
    web_app_info = WebAppInfo(url='https://uz.wikipedia.org/wiki/Chinoz_tumani')

    print(message.from_user.id, message.from_user.first_name, message.from_user.username)
    markup1 = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)

    markup1.add(KeyboardButton('📍chinoz tumani', web_app=web_app_info))


@dp.message_handler(Text('🥶Mahliyo sinim'))
async def keyboard_show_handler(message: types.Message):
    await message.answer(text='', reply_markup=main_btn())


@dp.message_handler(Text('📍chinoz tumani'))
async def keyboard_show_handler(message: types.Message):
    await message.reply_venue(address='https://uz.wikipedia.org/wiki/Chinoz_tumani', reply_markup=start_handler)


@dp.message_handler(Text('📒Contact'))
async def keyboard_show_handler(message: types.Message):
    await message.answer(text='Keyboard button show ', reply_markup=main_btn())


@dp.message_handler(Text('📍Location'))
async def keyboard_show_handler(message: types.Message):
    await message.answer(text='Keyboard button show ', reply_markup=main_btn())


@dp.message_handler(Text('🤵‍Tuman Hokimi'))
async def keyboard_show_handler(message: types.Message):
    await message.answer(text='Keyboard button show ', reply_markup=main_btn())


'''
@dp.message_handler(content_types='text')
async def test(message: types.Message):
    text = message.text
    text = text.lower()

    if text in salomlashish:
        await message.answer("Assalomu Alaykum")
    if text in xayrlashish:
        await message.answer("Xayr, Salomat bo'ling")
    # if text not in salomlashish and text not in xayrlashish:
    #     await message.reply(text="Kechirasiz , gapingizga tushunmadim")
'''

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

from aiogram import Dispatcher, types, Bot
from aiogram.utils import executor
from aiogram.types import ContentType
import os

bot = Bot(token=os.environ.get('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(content_types=ContentType.TEXT)
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Я буду повторять за тобой, <strong>{message.from_user.first_name}</strong>\n'
                           f'{message.text}',
                           parse_mode=types.ParseMode.HTML)


@dp.message_handler(content_types=ContentType.ANY)
async def fix_off(message: types.Message):
    await bot.send_message(message.from_user.id, text='Я понимаю только текст!\U0001F974')

if __name__ == '__main__':
    executor.start_polling(dp)

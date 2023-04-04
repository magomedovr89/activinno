from aiogram.types import ContentType
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from os import environ as env
from sql_base import *

bot = Bot(token=env['TOKEN'], parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def bot_text(message: types.Message) -> bot.send_message:
    cur.execute("SELECT telegram_id FROM homework")
    if message.from_user.id not in [user[0] for user in cur.fetchall()]:
        insert(message)
        return await message.answer(text=f'Привет, <b>{message.from_user.first_name}</b>🖐\nЯ бот - домашнее задание!\n'
                                         f'Я занес тебя в базу данных\n')
    else:
        return await message.answer(text=f'Привет, <b>{message.from_user.first_name}</b> 🖐\n'
                                         f'Вижу тебя в базе! 😁')


@dp.message_handler(content_types=ContentType.ANY)
async def bot_any(message: types.Message) -> bot.send_message:
    return await message.answer(
        text=f'Я понимаю только команду "/start", '
             f'{message.from_user.first_name}\n'
             f'¯\_(ツ)_/¯',
    )

if __name__ == '__main__':
    executor.start_polling(dp)

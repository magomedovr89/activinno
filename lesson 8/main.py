import db
import asyncio
import logging
import aiogram.utils.markdown as fmt
from data.db_session import global_init

from os import environ as env
from aiogram import Bot, Dispatcher, types
from datetime import datetime
from typing import Callable, Dict, Any, Awaitable
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message, CallbackQuery

BASE_URL = 'https://api.telegram.org/bot'
TOKEN = env['TOKEN']

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text


# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
   await message.answer(f"Привет, {message.from_user.full_name}")

@dp.message_handler(CommandHelp())
async def bot_start(message: types.Message):
   await message.answer(f"{message.from_user.full_name} вам нужна помощь?")

@dp.message_handler(Text(startswith='Бот'))
async def bot_start(message: types.Message):
   await message.answer(f"ВЫ ВВЕЛИ ТЕКСТ НАЧИНАЮЩИЙСЯ НА БОТ")

@dp.message_handler(Text(equals='телеграм'))
async def bot_start(message: types.Message):
   await message.answer(f"ВЫ ВВЕЛИ слово телеграмм")




def _is_weekend() -> bool:
   # 5 - суббота, 6 - воскресенье
   return datetime.utcnow().weekday() in (5, 6)


async def main():
    db_session = global_init('db/telegram_db.sqlite')
    dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
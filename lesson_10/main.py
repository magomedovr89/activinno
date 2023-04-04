import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat

import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text, Command
from os import environ as env
from filters import *




PROXY_URL = 'http://proxy.server:3128'
BASE_URL = 'https://api.telegram.org/bot'
TOKEN = env['TOKEN']
WEATHER_API = '352c751a80237a51813f0ae93d864822' #env['WEATHER_API']

logging.basicConfig(level=logging.INFO)

# Если вдруг запускаете на pythonanywhere расскомментировать
#bot = Bot(token=TOKEN, proxy=PROXY_URL, parse_mode=types.ParseMode.HTML)

# Если вдруг запускаете на pythonanywhere комментировать
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)



@dp.message_handler(IsPrivate(), Command(commands='private'))
async def start_bot(message: types.Message):
   await message.answer('Личный чат')


@dp.message_handler(IsGroup(), Command(commands='group'))
async def start_bot(message: types.Message):
   await message.answer('Групповой чат')


# # @dp.message_handler(commands=['start','hello'])
# # async def bot_start(message: types.Message):
# #    match message.text:
# #        case '/start':
# #            await message.answer(f"Бот запущен")
# #        case '/hello':
# #            await message.answer(f"Привет, {message.from_user.full_name}")
#
#
# # @dp.message_handler()
# # async def bot_start(message: types.Message):
# #    match message.text:
# #        case 'start':
# #            await message.answer(f"Бот запущен")
# #        case 'hello':
# #            await message.answer(f"Привет, {message.from_user.full_name}")
#
#
# @dp.message_handler(lambda message: message.text == 'Пока')
# async def bye(message: types.Message):
#     await message.answer('Пока')
#
# # async def set_default_commands(dp: Dispatcher):
# #     await dp.set_my_commands(types.BotCommand('set_description', 'Установить описание группы'))
#
# @dp.message_handler(IsPrivate(),  Command(commands='private'))
# async def start_bot(message: types.Message):
#    await message.answer('Личный чат')
#
# @dp.message_handler(commands='start')
# async def user_start(message: types.Message):
#    await message.reply('Hello')
#    await set_default_commands(bot)
#
#
# @dp.message_handler(commands='get_commands')
# async def user_start(message: types.Message):
#     await message.reply('Команда 2')
#
#
# @dp.message_handler(commands='reset_commands')
# async def user_start(message: types.Message):
#     await message.reply('Команда 3')


if __name__ == "__main__":
   # Запуск бота
   executor.start_polling(dp, skip_updates=True)

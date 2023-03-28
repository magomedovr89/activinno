# import logging
#
# from aiogram import Bot, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from aiogram.dispatcher import Dispatcher
# from aiogram.dispatcher.webhook import SendMessage
# from aiogram.utils.executor import start_webhook
# from os import environ as env
#
#
# API_TOKEN = env['TOKEN']
#
# # webhook settings
# WEBHOOK_HOST = 'адрес сайта'
# WEBHOOK_PATH = '/path/to/api'
# WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
#
# # webserver settings
# WEBAPP_HOST = 'localhost'  # or ip
# WEBAPP_PORT = 3001
#
# logging.basicConfig(level=logging.INFO)
#
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
# dp.middleware.setup(LoggingMiddleware())
#
#
# @dp.message_handler()
# async def echo(message: types.Message):
#    return SendMessage(message.chat.id, message.text)
#
#
# async def on_startup(dp):
#    await bot.set_webhook(WEBHOOK_URL)
#    # insert code here to run it after start
#
#
# async def on_shutdown(dp):
#    logging.warning('Shutting down..')
#
#    await bot.delete_webhook()
#
#    await dp.storage.close()
#    await dp.storage.wait_closed()
#
#    logging.warning('Bye!')
#
#
# if __name__ == '__main__':
#    start_webhook(
#        dispatcher=dp,
#        webhook_path=WEBHOOK_PATH,
#        on_startup=on_startup,
#        on_shutdown=on_shutdown,
#        skip_updates=True,
#        host=WEBAPP_HOST,
#        port=WEBAPP_PORT,
#    )


# import sqlite3
#
# con = sqlite3.connect("films_db.sqlite")
# cur = con.cursor()
# result = cur.execute("""SELECT *
#                         FROM films
#                         WHERE year = 2023""").fetchall()
#
# for elem in result:
#     print(elem)
# con.close()


# CREATE TABLE user (
#     id            INTEGER PRIMARY KEY,
#     is_bot        TEXT,
#     first_name    TEXT,
#     username      TEXT,
#     language_code TEXT
# );

from os import environ as env
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils.exceptions import BotBlocked
import time
import sqlite3

BASE_URL = 'https://api.telegram.org/bot'
TOKEN = env['TOKEN']

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)
con = sqlite3.connect('../db/telegram_db.sqlite')
cur = con.cursor()


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")
    return True


@dp.message_handler(commands="answer")
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message_handler(commands="reply")
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    info = message.values['from']
    try:
        result = cur.execute(f"""INSERT INTO user
                                (id, is_bot, first_name, username, language_code)
                                VALUES
                                ('{info['id']}', 
                                '{info['is_bot']}', 
                                '{info['first_name']}', 
                                '{info['username']}', 
                                '{info['language_code']}');""").fetchall()
        con.commit()
    except sqlite3.IntegrityError:
        print('Пользователь существует!!!')
    greet = cur.execute(f'''
                SELECT text
                FROM notebook
                WHERE command = 'start' AND lang = '{info["language_code"]}'; 
                ''').fetchone()
    #
    await message.answer(greet[0])


@dp.message_handler(commands=["test1"])
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


async def cmd_test2(message: types.Message):
    await message.reply("Test 2")


dp.register_message_handler(cmd_test2, commands="test2")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    con.close()

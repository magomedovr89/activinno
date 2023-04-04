from aiogram import Bot, executor, types, Dispatcher
from aiogram.types import ParseMode, ContentType
import os
bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'Привет <b>{message.from_user.first_name}</b>! 👋\n'
             f'Я бот - домашнее задание! ✔',
        parse_mode=ParseMode.HTML
    )


@dp.message_handler(commands='help')
async def cmd_help(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'Пока что, я ничего не умею!😅',
        parse_mode=ParseMode.HTML
    )


@dp.message_handler(content_types=ContentType.ANY)
async def any_content(message: types.Message):
    await message.answer(
        text=f'Я уже говорил, что ничего не умею? \U0001F915\n'
             f'Так вот, я ничего не умею! \U0001FAE3'
    )


if __name__ == '__main__':
    executor.start_polling(dp)

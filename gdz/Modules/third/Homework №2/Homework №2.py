import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ContentType


bot = Bot(token=os.environ['TOKEN'])
dp = Dispatcher(bot)


@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


@dp.message_handler(content_types=ContentType.ANY)
async def contenttype_any(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'Я понимаю только текст!')

if __name__ == '__main__':
    executor.start_polling(dp)

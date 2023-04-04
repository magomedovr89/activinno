from aiogram.types import ContentType
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from os import environ as env


bot = Bot(token=env['TOKEN'], parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text=f'Привет 🖐\nЯ бот - домашнее задание!\n'
                              f'Напишите мне что-то, а я буду вас дразнить!')


@dp.message_handler(content_types=ContentType.TEXT)
async def bot_text(message: types.Message):
    await message.answer(text=f'{message.text}')


@dp.message_handler(content_types=ContentType.ANIMATION)
async def bot_animation(message: types.Message) -> bot.send_message:
    return await message.answer_animation(animation=message.animation.file_id, caption='🤘')


@dp.message_handler(content_types=ContentType.PHOTO)
async def bot_animation(message: types.Message) -> bot.send_message:
    return await message.answer_photo(photo=message.photo[0].file_id, caption='🤘')


@dp.message_handler(content_types=ContentType.ANY)
async def bot_any(message: types.Message):
    await message.answer(
        text=f'Я понимаю только текст, фото и гифки, '
             f'{message.from_user.first_name}\n'
             f'¯\_(ツ)_/¯',
    )

if __name__ == '__main__':
    executor.start_polling(dp)

# /setname — Изменить имя робота.
# /setdescription — Изменить описание робота,
# представляющее собой короткий текст с описанием бота.
# Пользователи увидят его в самом начале, под заголовком «Что умеет этот робот?».
# /setabouttext — Изменить информацию о боте,
# ещё более короткий текст, отображающийся в профиле бота.
# Ещё, если кто-то поделится вашим ботом, то вместе со ссылкой на него отправится этот текст.
# /setuserpic — Изменить аватарку бота.
# /setcommands — Изменить список команд бота.
# Каждая команда состоит из собственно командного слова,
# начинающегося с символа косой черты («/») и короткого описания.
# Пользователи увидят список команд при вводе символа «/».
# /setjoingroups — Определяет, можно ли добавлять вашего бота в группы.
# /setprivacy — Определяет, все ли сообщения видит ваш бот в группах.
# В выключенном состоянии роботу будут отправляться все сообщения.
# /deletebot — Удалить бота и его имя пользователя.


#  '6020154315:AAGTUFF_H1oZvfMsCCxnKHpHh85RJHToULs'

#
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='')
dp = Dispatcher(bot)


@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply(f'Хватит писать всякую чепуху {message.from_user.first_name}')


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)

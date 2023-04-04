import logging
from aiogram import Bot, Dispatcher, executor, types
from os import environ as env

homework_ = {
    1: {
        2: {
            1: 'Modules/first/Урок - №2/1.py',
            2: 'Modules/first/Урок - №2/2.py',
            3: 'Modules/first/Урок - №2/3.py',
        }
    }
}

module_link = {
     1: 'first',
     2: 'second',
     3: 'third'
}
chapter_link = {key: f'Урок - №{key}' for key in range(2, 32)}


PROXY_URL = 'http://proxy.server:3128'
BASE_URL = 'https://api.telegram.org/bot'
TOKEN = env['TOKEN']
WEATHER_API = '352c751a80237a51813f0ae93d864822'  # env['WEATHER_API']
logging.basicConfig(level=logging.INFO)

# Если вдруг запускаете на pythonanywhere расскомментировать
# bot = Bot(token=TOKEN, proxy=PROXY_URL, parse_mode=types.ParseMode.HTML)

# Если вдруг запускаете на pythonanywhere комментировать
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)


@dp.message_handler(commands=['homework'])
async def get_homework(message: types.Message):
    module, chapter, task = map(int, message.text.split()[1:])
    print(f'Modules/{module_link[module]}/{chapter_link[chapter]}/{task}.py')
    open(f'Modules/{module_link[module]}/{chapter_link[chapter]}/{task}.py')
    try:
        await message.answer_document(open(f'Modules/{module_link[module]}/{chapter_link[chapter]}/{task}.py', mode='rb'))
    except:
        await message.reply('Что то не так. Во всем виноват Владимир')


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

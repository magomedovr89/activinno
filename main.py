import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat

import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text
from os import environ as env




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



async def set_starting_commands(bot: Bot, chat_id: int):
    STARTING_COMMANDS= {
        'ru': [
            BotCommand('start', 'Начать заново'),
            BotCommand('get_commands', 'Получить список команд'),
            BotCommand('reset_commands', 'Сбросить команды')
        ],
        'en': [
            BotCommand('start', 'Restart bot'),
            BotCommand('get_commands', 'Retrieve command list'),
            BotCommand('reset_commands', 'Reset commands')
        ]
    }
    for language_code, commands in STARTING_COMMANDS.items():
        await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeChat(chat_id),
            language_code=language_code

        )

@dp.message_handler(commands='start')
async def user_start(message: types.Message):
   await message.reply('Hello')
   await set_starting_commands(bot, message.from_user.id)


@dp.message_handler(commands=['get_commands'])
async def message_get_command(message: types.Message):
   # no_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id))
   no_args = await message.bot.get_my_commands()
   ru_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id), language_code='ru')

   await message.reply(f'{[[i for i in arg] for arg in no_args]}')

async def force_reset_all_commands(bot: Bot):
    for language_code in ('ru', 'en', 'el'):
        for scope in (
                BotCommandScopeDefault(),
                BotCommandScopeAllPrivateChats(),
                BotCommandScopeAllGroupChats(),
                BotCommandScopeAllChatAdministrators(),
        ):
            await bot.delete_my_commands(scope, language_code)


@dp.message_handler(commands='reset_commands')
async def user_start(message: types.Message):
    await message.reply('exit 3')


if __name__ == "__main__":
   # Запуск бота
   executor.start_polling(dp, skip_updates=True)


# @dp.message_handler()
# async def get_weather(message: types.Message):
#
#    code_to_smile = {
#        "Clear": "Ясно \U00002600",
#        "Clouds": "Ясно \U00002601",
#        "Rain": "Дождь \U00002614",
#        "Drizzle": "Дождь \U00002614",
#        "Thunderstorm": "Гроза \U000026A1",
#        "Snow": "Снег \U0001F328",
#        "Mist": "Туман \U0001F32B"
#    }
#    try:
#        url = 'https://api.openweathermap.org/data/2.5/weather'
#        params = {'APPID': WEATHER_API,
#                  'q': message.text,
#                  'units': 'metric',
#                  'lang': 'ru'}
#        r = requests.get(url, params=params)
#
#        data = r.json()
#        print(data)
#        city = data['name']
#
#        cur_weather = data['main']['temp']
#
#        weather_description = data['weather'][0]['main']
#        if weather_description in code_to_smile:
#            wd = code_to_smile[weather_description]
#        else:
#            wd = 'Посмотри в окно сам'
#
#        humidity = data['main']["humidity"]
#        pressure = data['main']['pressure']
#        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
#        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
#        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - \
#                            datetime.datetime.fromtimestamp(data['sys']['sunrise'])
#        wind = data['wind']['speed']
#
#
#        await message.answer(f'***{datetime.datetime.now().strftime("%d.%m.%Y %H:%M")}***\n'
#              f'Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n'
#              f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/c\n'
#              f'Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n'
#              f'Хорошего дня!')
#    except Exception as err:
#        await message.reply('Проверьте название города!')
#
# if __name__ == '__main__':
#    executor.start_polling(dp)

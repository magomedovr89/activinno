from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, code
from aiogram.types import ParseMode
from aiogram.types import InlineKeyboardMarkup, \
    InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import CallbackQuery
from config import TOKEN
import requests
from database import *
from aiogram.dispatcher.filters import Text


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])  # Декоратор для команды /start
async def send_welcome(message: types.Message):  # Функция для обработки /start
    print(f'/start\nid пользователя - "{message.from_user.id}" \nusername пользователя "{message.from_user.username}"'
          f'\n{"_" * 1000}')
    user = text(bold(message.from_user.first_name))  # Получаем имя пользователя толстым шрифтом
    markup = InlineKeyboardMarkup(resize_keyboard=True)  # Создаём макеты для отображения кнопок
    markup.add(InlineKeyboardButton(text='help', callback_data='help'))  # Добавляем кнопку help
    sql.execute("SELECT id FROM base")
    if message.from_user.id not in [int(str(i)[1:len(i)-3]) for i in sql.fetchall()]:
        if message.from_user.username is None:
            sql.execute("SELECT * FROM base WHERE id =?", (message.from_user.id,))
            sql.execute("INSERT INTO base VALUES (?,?,?,?)", ("IsNone", message.from_user.id, 'None', 1))
        else:
            sql.execute("SELECT * FROM base WHERE id =?", (message.from_user.id,))
            sql.execute("INSERT INTO base VALUES (?,?,?,?)",
                        (message.from_user.username, message.from_user.id, 'None', 1))
        db.commit()
        await bot.send_message(message.from_user.id,
                               f'Привет, {user} \U0001F609 !\n'
                               f'Я Telegram-бот для получения погоды в твоем регионе. '
                               f'Для получения всех команд, которые я понимаю, нажмите "help".'
                               f'\nИли пропишите команду /help.\n',
                               parse_mode=ParseMode.MARKDOWN, reply_markup=markup)
        await bot.send_message(message.from_user.id,
                               f'Вижу ты тут впервые, напишите регион который будет вашим основным'
                               f' для получения погоды.'
                               f'\nНапишите "{text(code("/setcity city"),sep=" ")}" '
                               f'где city - город, например, "Москва".'
                               f'\nТак же ты можешь написать любой регион, а я отправлю погоду в этом регионе \U000026C5', parse_mode=ParseMode.MARKDOWN)
    else:
        print('id уже есть в базе', message.from_user.id, message.from_user.username)
        await bot.send_message(message.from_user.id, f'Привет, {user} \U0001F609!\n'
                                                     f'Я тебя помню!\n'
                                                     f'Нажми "help" для ознакомления с командами.\n'
                                                     f'Напиши регион для получения погоды \U000026C5\n'
                                                     f'Если у тебя уже выставлен регион просто напиши "погода".',
                               reply_markup=markup, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['setcity'])  # Декоратор для команды /setcity
async def set_city(message: types.Message):  # Функция для обработки /setcity
    city = str(message.text[9::]).capitalize()  # Срез текста сообщения, для получения города
    if len(city) <= 1:  # Проверка на точно не существующие города или страны
        await message.reply(f'\U0001F915 Название региона слишком короткое!', parse_mode=ParseMode.MARKDOWN)
    else:
        try:  # Обработка ошибки если такого региона не существует
            city = message.text[9::].capitalize()  # Срез текста сообщения
            url = 'https://api.openweathermap.org/data/2.5/weather'
            api_of_weather = '352c751a80237a51813f0ae93d864822'
            params = {'APPID': api_of_weather,
                      'q': city,
                      'units': 'metric',
                      'lang': 'ru'}
            result = requests.get(url, params=params).json()  # Запрос на получение данных
            # Если город существует, вернет словарь с длинной больше 2
            if len(result) < 3:
                raise ValueError('Город не существует')

            if message.from_user.username is None:
                sql.execute("SELECT * FROM base WHERE id =?", (message.from_user.id,))
                sql.execute(f"REPLACE INTO base (username, id, city, active) VALUES (?,?,?,?)", (
                    'IsNone', message.from_user.id, city, 1,))

            else:
                sql.execute("SELECT * FROM base WHERE id =?", (message.from_user.id,))
                sql.execute(f"REPLACE INTO base (username, id, city, active) VALUES (?,?,?,?)", (
                    message.from_user.username, message.from_user.id, city, 1,))
            db.commit()
            await bot.send_message(message.from_user.id,
                                   f'Город установлен!\n'
                                   f'Ваш регион: {city}\n', reply_markup=get_weather_button())
            print(f'setcity: ({message.from_user.username}: {str(city)})')
            print(f'{"_" * 1000}')  # Выводим данные о пользователе и городе
        except:
            await message.reply(f'Что-то пошло не так!\U0001F915', parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['mycity'])
async def my_city(message: types.Message):  # Обычный вывод установленного города
    city = str(list(sql.execute("SELECT city FROM base WHERE id =?", (message.from_user.id,))))
    city = city[3:len(city)-4]
    if city == 'None' or len(city) == 0:
        await bot.send_message(message.from_user.id,
                               f'У вас не установлен регион!')
    else:
        await bot.send_message(message.from_user.id,
                               f'Ваш регион: {city}', reply_markup=get_weather_button())
        print(f'Вызвана команда my_city:\n({message.from_user.username}:'
              f'{city}\n{"_" * 1000}')


@dp.callback_query_handler(text='help')  # Обработка callback из кнопки help в сообщении /start
async def help_in_welcome(call: CallbackQuery):
    await bot.send_message(call.from_user.id, f'Я понимаю эти команды:\n'
                                              f'{text(code("/start"))}\n'
                                              f'{text(code("/help"))}\n'
                                              f'{text(code("/developer"))}\n'
                                              f'{text(code("/setcity"))}\n'
                                              f'{text(code("/mycity"))}\n'
                                              f'Для получения погоды напишите желаемый регион.\n'
                                              f'Для получения погоды в установленном регионе напишите "погода"',
                           parse_mode=ParseMode.MARKDOWN)


def get_weather_button() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Погода'))


@dp.message_handler(Text(equals='Погода', ignore_case=True))
async def weather(message: types.Message):  # Выводим данные погоды для установленного города
    try:
        sql.execute("SELECT city FROM base WHERE id =?", (message.from_user.id,))
        city = sql.fetchone()[0]
        url = 'https://api.openweathermap.org/data/2.5/weather'
        api_of_weather = '352c751a80237a51813f0ae93d864822'
        params = {'APPID': api_of_weather,
                  'q': city,
                  'units': 'metric',
                  'lang': 'ru'}
        result = requests.get(url, params=params).json()
        info = result['main']['temp'], result['main']['feels_like'], result['weather'][0]['description'], result['name']
        print(f'"Погода":\nid - {message.from_id}, Тег - {message.from_user.username}, '
              f'Имя - {message.from_user.first_name}\n{info}\n{"_" * 1000}')
        await bot.send_message(message.from_user.id,
                               f'Погода в регионе <strong>{info[3]}</strong>:\n'
                               f'<em><strong>{info[0]} °C, ощущается как {info[1]}°C, {info[2]}</strong></em>',
                               parse_mode=ParseMode.HTML)
    except KeyError:
        await bot.send_message(message.from_user.id,
                               f'Что-то пошло не так!\U0001F915',
                               parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['help'])  # Вывод команд /help
async def send_help(message: types.Message):
    await bot.send_message(message.from_user.id, f'Я понимаю эти команды:\n'
                                                 f'{text(code("/start"))}\n'
                                                 f'{text(code("/help"))}\n'
                                                 f'{text(code("/developer"))}\n'
                                                 f'{text(code("/setcity"))}\n'
                                                 f'{text(code("/mycity"))}\n'
                                                 f'Для получения погоды напишите желаемый регион.\n'
                                                 f'Для получения погоды в установленном регионе напишите "погода"',
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['message'])  # Рассылка погоды для пользователей и их установленных городов
async def send_message(message: types.Message):
    if message.from_user.id == 790528433:
            url = 'https://api.openweathermap.org/data/2.5/weather'
            api_of_weather = '352c751a80237a51813f0ae93d864822'
            sql.execute("SELECT id FROM base")
            for user_id in sql.fetchall():
                user_id = int(str(user_id)[1:len(str(user_id)) - 2])
                try:
                    try:
                        if user_id not in [875776158]:
                            sql.execute("SELECT city FROM base WHERE id =?", (user_id,))
                            city = sql.fetchone()[0]
                            username = sql.execute("SELECT username FROM base WHERE id =?", (user_id,))
                            print(f'{city} - Рассылка\n{user_id} @{sql.fetchone()[0]}')
                            params = {'APPID': api_of_weather,
                                      'q': city,
                                      'units': 'metric',
                                      'lang': 'ru'}
                            result = requests.get(url, params=params).json()
                            info = (result['main']['temp'], result['main']['feels_like'],
                                    result['weather'][0]['description'], result['name'])
                            print(f'{info}\n{"_" * 1000}')
                            await bot.send_message(chat_id=user_id,
                                                   text=f'Погода в регионе <strong>{info[3]}</strong>:\n'
                                                   f'<em><strong>{info[0]} °C, ощущается как {info[1]}'
                                                   f'°C, {info[2]}</strong></em>',
                                                   parse_mode=ParseMode.HTML)
                            sql.execute("SELECT active FROM base WHERE id =?", (user_id,))
                            if int(str(sql.fetchone())[1:2]) == 0:
                                sql.execute(f"UPDATE base SET active = {1} WHERE id =?", (user_id,))
                                db.commit()
                    except KeyError:
                        await bot.send_message(chat_id=user_id, text=f'Неверное установлен регион!')
                except:
                    sql.execute("UPDATE base SET active = 0 WHERE id =?", (user_id,))
                    db.commit()


@dp.message_handler(commands=['developer'])  # Вывод команды /developer
async def send_developer(message: types.Message):
    buttons = types.InlineKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons.add(types.InlineKeyboardButton('Вавилон', url='https://t.me/w1thoutiq'))
    await bot.send_message(message.from_user.id, text='<strong>Я тут!\n@w1thoutiq</strong>',
                           reply_markup=buttons, parse_mode=ParseMode.HTML)


# Обработка любого текста, если есть город, то вернет погоду пользователю
@dp.message_handler(content_types=ContentType.TEXT)
async def unknown_message(message: types.Message):
    try:
        city = message["text"].capitalize()
        url = 'https://api.openweathermap.org/data/2.5/weather'
        api_of_weather = '352c751a80237a51813f0ae93d864822'
        params = {'APPID': api_of_weather,
                  'q': city,
                  'units': 'metric',
                  'lang': 'ru'}
        result = requests.get(url, params=params).json()
        info = result['main']['temp'], result['main']['feels_like'], result['weather'][0]['description'], result['name']
        print(f'Город из текста "{city}":\nid - {message.from_id}, Тег - @{message.from_user.username}, '
              f'Имя - {message.from_user.first_name}\n{info}\n{"_" * 1000}')
        await bot.send_message(message.from_user.id,
                               f'Погода в регионе <strong>{info[3]}</strong>:\n'
                               f'<em><strong>{info[0]} °C, ощущается как {info[1]}°C, {info[2]}</strong></em>',
                               parse_mode=ParseMode.HTML)
    except KeyError:
        await message.reply(f'\U0001F915Страна или регион указан неверно!', parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(content_types=ContentType.ANY)  # Обработка любого типа сообщений, что-бы избежать лишних ошибок
async def unknown_message(msg: types.Message):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    markup.add(InlineKeyboardButton(text='help', callback_data='help'))
    await msg.reply(f'Я не знаю что с этим делать, но напоминаю,\n'
                    f'что вы можете использовать команду "/help"',
                    parse_mode=ParseMode.MARKDOWN, reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp)  # Бесконечный цикл для работы бота

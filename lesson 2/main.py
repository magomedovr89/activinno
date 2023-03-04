from os import environ as env
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils.exceptions import BotBlocked
import time


BASE_URL = 'https://api.telegram.org/bot'
TOKEN = env['TOKEN']
ADMINS = [910372170]

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



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
    time.sleep(5)
    await message.answer("Hello!")


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











# def pulling():
#    count_message = 0
#    while True:
#        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
#        if count_message != len(response['result']):
#            count_message = len(response['result'])
#            message = response['result'][-1]
#            file_id = message['message']['video']['file_id']
#            user_id = message['message']['from']['id']
#            pprint(response)
#            if user_id in ADMINS:
#                requests.get(f'{BASE_URL}{TOKEN}/sendVideo?chat_id={user_id}&video={file_id}')
#                break
#

#
# def pulling():
#    count_message = 0
#    while True:
#        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
#        if count_message != len(response['result']):
#            count_message = len(response['result'])
#            message = response['result'][-1]
#            file_id = message['message']['voice']['file_id']
#            user_id = message['message']['from']['id']
#            pprint(response)
#            if user_id in ADMINS:
#                requests.get(f'{BASE_URL}{TOKEN}/sendVoice?chat_id={user_id}&voice={file_id}')
#                break
#
# pulling()

# def pulling():
#    count_message = 0
#    while True:
#        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
#        if count_message != len(response['result']):
#            count_message = len(response['result'])
#            message = response['result'][-1]
#            user_id = message['message']['from']['id']
#            if user_id in ADMINS:
#                requests.get(f'{BASE_URL}{TOKEN}/sendContact?chat_id={user_id}&phone_number=89911904125&first_name=Ivan')

# pulling()


# def pulling():
#    count_message = 0
#    while True:
#        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
#        if count_message != len(response['result']):
#            count_message = len(response['result'])
#            message = response['result'][-1]
#            user_id = message['message']['from']['id']
#            if user_id in ADMINS:
#                requests.get(f'{BASE_URL}{TOKEN}/sendLocation?chat_id={user_id}&latitude=55.53932&longitude=37.39892')


# def pulling():
#    count_message = 0
#    while True:
#        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
#        if count_message != len(response['result']):
#            count_message = len(response['result'])
#            message = response['result'][-1]
#            user_id = message['message']['from']['id']
#            if user_id in ADMINS:
#                requests.get(f'{BASE_URL}{TOKEN}/sendVenue?chat_id={user_id}&latitude=55.53932&longitude=37.39892&title=Moscow')


# def pulling():
#    count_message = 0
#    while True:
#        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
#        if count_message != len(response['result']):
#            count_message = len(response['result'])
#            message = response['result'][-1]
#            user_id = message['message']['from']['id']
#            if user_id not in ADMINS:
#
#                r = requests.get(f'{BASE_URL}{TOKEN}/getUSerProfilePhotos?user_id={user_id}').json()
#                if r:
#                    continue
#                file_id = r['result']['photos'][0][-1]['file_id']
#                requests.get(f'{BASE_URL}{TOKEN}/sendPhoto?chat_id={user_id}&photo={file_id}&caption={user_id}')


# def pulling():
#    count_message = 0
#    while True:
#        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
#        if count_message != len(response['result']):
#            count_message = len(response['result'])
#            message = response['result'][-1]
#            user_id = message['message']['from']['id']
#            requests.post(f"{BASE_URL}{TOKEN}/",
#                          json={'method': 'sendMessage', 'chat_id': f'{user_id}', 'text': 'Обычная клавиатура',
#                                'reply_markup': {'keyboard': [[{'text': 'Yes'}, {'text': 'No'}]],'resize_keyboard': True, 'one_time_keyboard': True},
#                               })
#            # break
#
# pulling()

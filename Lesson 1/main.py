# import os
# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
#
# bot = Bot(token=os.environ['TOKEN'])
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands="test1")
# async def cmd_test1(message: types.Message):
#    await message.reply("Все что угодно моей душе")
#
#
# @dp.message_handler()
# async def echo_message(msg: types.Message):
#    await bot.send_message(msg.from_user.id, msg.text)
#
#
# if __name__ == '__main__':
#    executor.start_polling(dp)
import os

# import shutil
# import requests
#
# url = 'https://static-maps.yandex.ru/1.x/?ll=47.523192,42.973909&spn=0.016457,0.00619&l=map'
# r = requests.get(url, stream=True)
# r.raise_for_status()
# r.raw.decode_content = True
# with open('picture.png', 'wb') as file:
#     shutil.copyfileobj(r.raw, file)


# https://api.telegram.org/bot<token>/НАЗВАНИЕ_МЕТОДА

# Допускаются GET и POST запросы. Для передачи параметров в Bot API доступны 4 способа:
# Запрос в URL
# application/x-www-form-urlencoded
# application/json (не подходит для загрузки файлов)
# multipart/form-data (для загрузки файлов)


# import requests
# import os
# from pprint import pprint
#
# BASE_URL = 'https://api.telegram.org/bot'
#
# TOKEN = os.environ['TOKEN']
#
#
# def get_updates():
#    r = requests.get(f'{BASE_URL}{TOKEN}/getUpdates?offset=15&timeout=10')
#    pprint(r.json())
#
#
# get_updates()
#
#

# import requests
#
# BASE_URL = 'https://api.telegram.org/bot'
#
# TOKEN = os.environ['TOKEN']
# ADMINS = [910372170]
#
#
# def pulling():
#     count_message = 0
#     while True:
#         response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
#         if count_message != len(response['result']):
#             count_message = len(response['result'])
#             message = response['result'][-1]
#             user_id = message['message']['from']['id']
#             user_name = message['message']['from']['username']
#             # text = message['message']['text']
#             # if user_id in ADMINS and text == '/test1':
#             #     requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text=Привет {user_name}   {message}')
#             file_id = message['message']['photo'][-1]['file_id']
#
#             caption = message['message']['caption']
#             user_id = message['message']['from']['id']
#             user_name = message['message']['from']['username']
#             if user_id in ADMINS:
#                 requests.get(f'{BASE_URL}{TOKEN}/sendPhoto?chat_id={user_id}&photo={file_id}&caption={caption}')
#
#
# pulling()

import requests

BASE_URL = 'https://api.telegram.org/bot'

TOKEN = os.environ['TOKEN']
ADMINS = [910372170]
def pulling():
   count_message = 0
   while True:
       response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
       if count_message != len(response['result']):
           count_message = len(response['result'])
           message = response['result'][-1]
           file_id = message['message']['photo'][-1]['file_id']
           caption = message['message']['caption']
           user_id = message['message']['from']['id']
           user_name = message['message']['from']['username']
           if user_id in ADMINS:
               requests.get(f'{BASE_URL}{TOKEN}/sendPhoto?chat_id={user_id}&photo={file_id}&caption={caption}')

pulling()



# import os
#
# print(os.environ['TOKEN'])

import requests
import os

TOKEN = os.environ.get('TOKEN')
BASE_URL = 'https://api.telegram.org/bot'


def pulling():
    count_message = 0
    while True:
        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        if count_message != len(response['result']):
            count_message = len(response['result'])
            message = response['result'][-1]
            user_id = message['message']['from']['id']
            user_name = message['message']['from']['username']
            text = message['message']['text']
            if user_id:
                requests.get(f'{BASE_URL}{TOKEN}/sendMessage?chat_id={user_id}&text={message["message"]["text"]}')


pulling()

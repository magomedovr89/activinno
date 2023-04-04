import os
import requests
TOKEN = os.environ['TOKEN']
BASE_URL = 'https://api.telegram.org/bot'


def pooling():
    count_message = 0
    while True:
        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        if count_message != len(response['result']):
            count_message = len(response['result'])
            message = response['result'][-1]
            user_id = message['message']['from']['id']
            text_message = message['message']['text']
            requests.get(
                f"{BASE_URL}{TOKEN}/",
                json={
                    'method': 'SendMessage',
                    'chat_id': user_id,
                    'user_id': user_id,
                    'text': text_message
                }
            )
pooling()


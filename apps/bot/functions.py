from telegram_api.settings import TELEGRAM_BOT_TOKEN
import requests


def send_message_telegram(chat_id, text):
    URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    r = requests.post(URL, data=data)
    return r.json()


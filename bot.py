# Библиотека для работы с запросами HTTP
import requests
# Библиотека для работы с json
# import json

# Для теста aiogram
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command



# библиотеки для игровой части
# from telegram import InlineQueryResultArticle, InputTextMessageContent
# from telegram.ext import Updater, InlineQueryHandler, CommandHandler

# Токен, идентификатор бота, по нему api определяет с 
# каким ботом работать amator4DedBot
TOKEN = '6754939943:AAFvmhs3KjuEbz37_BOgbxHWp5kL15x4WBQ'
# Базовый запрос с отформатированной строкой.
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/'

# Функция с необязательным параметром offset
def get_updates(offset=None):
    # К основному пути, который содержит адрес апи телеграмма и
    # токена, добавляется метод, который должен будет отработать.
    # Данный конкретный метод возвращает обновление инфы в чате.
    url = BASE_URL + 'getUpdates'
    # Параметры получения обновления, offset указывает на 
    # следующее новое обновление. В этой переменной будет программа
    # хранить id последнего обработанного изменения.
    params = {'offset': offset, 'timeout': 100}
    # Непосредственно гет запрос к апи
    response = requests.get(url, params=params)
    # Вернуть json ответ от гет запросса
    return response.json()

# parse_mode='HTML'
def send_message(chat_id, text):
    url = BASE_URL + 'sendMessage'
    data = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
    response = requests.post(url, data=data)
    return response.json()


def main():
    # начальный указатель идентификатора информации в чате
    offset = None
    # Бесконечный цикл
    while True:
        # Получить обновление
        updates = get_updates(offset)
        # Если в результирующем массиве есть индекс result
        # и он не пустой
        if 'result' in updates and updates['result']:
            # Просмотреть все обновления
            for update in updates['result']:
                if 'message' in update and 'text' in update['message']:
                    chat_id = update['message']['chat']['id']
                    message_text = update['message']['text']

                    if ('гит' in message_text 
                        or 'git' in message_text):
                        result = '<a href="https://github.com/dfdxAlex">Git</a>'
                    elif 'сайт' in message_text.lower():
                        result = '<a href="http://amatorded.pl">Сайт amatorded.pl</a>'
                    elif 'dfdx' in message_text.lower():
                        result = '<a href="http://127.0.0.1:81/redaktor/dfdx/dfdx.php">Сайт DFDX</a>'
                    elif 'cv' in message_text.lower():
                        result = '<a href="http://127.0.0.1:81/redaktor/CV/public/cv.php">CV креатор</a>'
                    elif 'chcę kupić lamp' in message_text.lower() or 'chce kupic lampe' in message_text.lower() or 'kupic lampe' in message_text.lower():
                        result = 'Swietny pomysł, mogę spróbować doradzić Ci w tej kwestii'
                    elif 'dzień dobry' in message_text.lower() or 'dzien dobry' in message_text.lower():
                        result = 'Dzień dobry. Czy mogę ci w czymś pomóc?'
                    else:
                        result = '<b>Dzień dobry, jestem chat botem sklepu, cudny lampy. Mogę spróbować ci pomóc. Proszę zadać pytanie.</b>'

                    send_message(chat_id, result)
                    offset = update['update_id'] + 1


if __name__ == '__main__':
    main()


# создать виртуальное окружение
# python -m venv myenv
# активировать
# myenv/Scripts/activate
# установить в окружение
# pip install python-telegram-bot
# deactivate

# Установить библиотеку Requests
# pip install requests

# Установка библиотеки aiogram
# pip install -U aiogram

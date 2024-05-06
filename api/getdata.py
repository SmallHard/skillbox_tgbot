import sqlite3
import requests
from handlers.custom_handlers.getdata import bot_get_data


# def fetch_and_insert_data():
#     try:
#         data = bot_get_data()
#         return data
#     except requests.exceptions.RequestException as e:
#         return f'Произошла ошибка при получении данных от API. {e}'
#     except sqlite3.Error as e:
#         return f'Произошла ошибка при записи данных в базу данных. {e}'
#     except Exception as e:
#         return f'Произошла непредвиденная ошибка. {e}'
#
#

import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
    ("low", "Вывод минимальных показателей"),
    ("high", "Вывод максимальных показателей"),
    ("custom", "Вывод показателей пользовательского диапазон"),
    ("history", "Вывод истории запросов пользователей"),
    ("getdata", "Получение данных с сайта")
)

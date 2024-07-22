import sqlite3 as sq
from loader import db_storage


async def db_start(user_name):
    create_base = sq.connect(db_storage)
    with create_base as db:
        cursor = db.cursor()
        cursor.execute(f'''CREATE TABLE IF NOT exists {user_name}(user_name TEXT, commands TEXT)''')
        db.commit()

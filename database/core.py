import sqlite3 as sq
from loader import db_storage

async def db_start():
    create_base = sq.connect(db_storage)
    with create_base as db:
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT exists users(user_id TEXT, user_name TEXT, commands TEXT)''')
        db.commit()


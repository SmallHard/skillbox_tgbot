import sqlite3 as sq
from loader import db_storage


async def history(user_name, command):
    with sq.connect(db_storage) as db:
        cursor = db.cursor()
        cursor.execute(f'''INSERT INTO {user_name}(user_name, commands) VALUES (?, ?)''',
                       (str(user_name), str(command)))
        db.commit()

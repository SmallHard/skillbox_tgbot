import sqlite3 as sq
from loader import db_storage



async def history(user_id, user_name, commands):
        db = sq.connect(db_storage)
        cursor = db.cursor()
        cursor.execute('''INSERT INTO users(user_id, user_name, commands) VALUES (?, ?, ?)''', (user_id, user_name, commands))
        db.commit()
        db.close()


async def history_exited():
    conn = sq.connect('../base.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    user_data = cur.fetchall()
    user_str = "\n".join([str(data) for data in user_data])
    conn.close()
    return user_str
    
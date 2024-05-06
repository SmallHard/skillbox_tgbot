import sqlite3


def add_to_history(user_id, command):
    conn = sqlite3.connect('../base.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history
                 (user_id text, command text)''')
    c.execute("INSERT INTO history VALUES (?, ?)", (user_id, command))
    conn.commit()
    conn.close()


def get_history(user_id):
    conn = sqlite3.connect('../base.db')
    c = conn.cursor()
    c.execute("SELECT command FROM history WHERE user_id=? ORDER BY rowid DESC LIMIT 10", (user_id,))
    history = c.fetchall()
    conn.close()
    return [command[0] for command in history]

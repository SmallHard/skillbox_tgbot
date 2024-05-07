import sqlite3


class DatabaseManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS api_data (
            id INTEGER PRIMARY KEY, data TEXT)''')
        self.conn.commit()

    def close(self):
        self.conn.close()


class CRUD:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def read_data(self):
        self.db_manager.cursor.execute('SELECT * FROM api_data')
        rows = self.db_manager.cursor.fetchall()
        return rows

    def insert_data(self, data):
        self.db_manager.cursor.execute('INSERT INTO api_data (data) VALUES (?)', (data,))
        self.db_manager.conn.commit()


def create_base():
    db = DatabaseManager(db_path='../base.sql')
    return db


create_base()

import sqlite3

DATABASE = 'students.db'

def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection

def init_db():
    connection = get_db_connection()
    connection.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done INTEGER NOT NULL DEFAULT 0 CHECK (done IN (0,1)),
        priority INTEGER NOT NULL DEFAULT 3 CHECK (priority IN (1,5))
        )
    ''')

    connection.commit()
    connection.close()

init_db()
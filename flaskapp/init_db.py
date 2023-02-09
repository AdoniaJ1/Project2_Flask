import sqlite3
connection = sqlite3.connect('database.db')
cur = connection.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, firstname TEXT, lastname  TEXT, email  TEXT)''')

connection.commit()
connection.close()

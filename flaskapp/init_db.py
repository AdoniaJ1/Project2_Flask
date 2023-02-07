import sqlite3
connection = sqlite3.connect('database.db')

connection.execute('DROP TABLE IF EXISTS users')
connection.execute('CREATE TABLE users (username TEXT, password TEXT, firstname TEXT, lastname  TEXT, email  TEXT)')

connection.commit()
connection.close()

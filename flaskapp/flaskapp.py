from flask import Flask,render_template,request
from collections import Counter
import csv
import sqlite3
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def hello_world():
  return 'Hello from Flask!'

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/registered', methods = ['POST','GET'])
def registered():
    if request.method == "POST":
        try:
            with sqlite3.connect("database.db") as con:
                msg = "Record successfully added"
        except:
            msg = "error in insert operation"
        finally:
            con.close()
    return render_template("registered.html",msg = msg)
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/display',methods = ['POST', 'GET'])
def display():
    username = request.form['username']
    password = request.form['password']
    conn = get_db_connection()
    msg = conn.execute("SELECT firstname,lastname,email FROM users WHERE username=? and password=?",(username,password))
    return 'yuck'
if __name__ == '__main__':
    app.run()


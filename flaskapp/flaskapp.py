from flask import Flask,render_template,request,send_file,url_for
from collections import Counter
import os
from array import *
app = Flask(__name__)

users = []
@app.route("/")
def woof():
    return 'woof'

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/registered', methods = ['POST','GET'])
def registered():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        user = [username,password,firstname,lastname,email]
        users.append(user)
        msg = "{fname} {lname} registered \nUsername:{un} \nPassword:{pwrd}\n Email: {email}".format(fname = firstname, lname= lastname, un=username, pwrd=password, email=email)
        document_path = '/home/ubuntu/flaskapp/Limerick.txt'
        number_of_words = 0
        document = open(document_path, 'r')
        contents = document.read()
        lines = contents.split()
        number_of_words += len(lines)
        msg = msg +  "\n# of words in Limerick are: {num}".format(num = number_of_words)
    return render_template("registered.html",msg=msg)
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/download')
def download_file():
	path = "Limerick.txt"
	return send_file(path, as_attachment=True)
@app.route('/display',methods = ['POST', 'GET'])
def display():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        msg = 'No user found :('
        
        for i in users:
            if i[0]==username and i[1]==password:
                msg ="Hello, {fname} {lname}, your information is Username:{un} Password:{pwrd} Email: {email}".format(fname = i[2], lname= i[3], un=username, pwrd=password, email=i[4])
        document_path = '/home/ubuntu/flaskapp/Limerick.txt'
        number_of_words = 0
        document = open(document_path, 'r')
        contents = document.read()
        lines = contents.split()
        number_of_words += len(lines)
        msg = msg +  "\n# of words in Limerick are: {num}".format(num = number_of_words)
    return render_template("display.html",msg=msg)
if __name__ == '__main__':
    app.run()


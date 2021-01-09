import mysql.connector
from flask import Flask, render_template,request,session
import os
from decouple import config

db =mysql.connector.connect(
    host = config('HOST'),
    user = config('USER'),
    passwd = config('PASSWORD'),
    database = config('DATABASE')
)

app = Flask(__name__)

#mycursor = db.cursor()
#mycursor.execute("CREATE TABLE User(Username VARCHAR(50), Password VARCHAR (10), personID int PRIMARY KEY AUTO_INCREMENT)")
#db.commit()
@app.route("/")
def index():

    return "hello"

if __name__ == '__main__':
    app.run(port=50000, debug=True) 
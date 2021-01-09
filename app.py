import mysql.connector
from flask import Flask, render_template,request,session
import os

db =mysql.connector.connect(
    host = "localhost",
    user = "root" ,
    passwd = "root",
    database = "deliverdatabase"
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
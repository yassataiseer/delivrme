import mysql.connector
import os

from decouple import config

db =mysql.connector.connect(
    host = config('HOST'),
    user = config('USER'),
    passwd = config('PASSWORD'),
    database = config('DATABASE')
)
mycursor = db.cursor()


class user:

    def add_user(user,password):
        mycursor.execute("INSERT INTO user (Username,Password) VALUES (%s,%s)",(user,password))
        db.commit()
        print("Succesfully added")

    
    def check_user(user,password):
        pass

user.add_user("Yassa Taiseer","yassa123")
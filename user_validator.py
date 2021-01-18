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
    def add_user(username,password):
        boolean = user.check_if_user_exists(username)
        if boolean == True:
            return False
        mycursor.execute("INSERT INTO user (Username,Password) VALUES (%s,%s)",(username,password))
        db.commit()
        return True

    def check_user(user,password):
        mycursor.execute("SELECT Username FROM user WHERE Username = (%s) AND Password = (%s) ",(user,password))
        data = mycursor.fetchall()
        if len(data)==0:
            return False
        else:
            return True
        
    def check_if_user_exists(user):
        mycursor.execute("SELECT Username FROM user WHERE Username = (%s) ",(user,))
        data = mycursor.fetchall()
        if len(data)==0:
            return False
        else:
            return True

#print(user.check_user("Eshal Taiseer","eshal123"))
print(user.check_if_user_exists("Taiseer Taiseer"))
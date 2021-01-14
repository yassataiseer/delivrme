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


class order:
    def delete_order(Username,Address,Item,Price,User_Info):
        mycursor.execute("DELETE FROM deliveries WHERE Username = %s AND Address = %s AND Item = %s AND Price = %s AND User_Info = %s",(Username,Address,Item,Price,User_Info))
        db.commit()
        return True
    def add_order(Username,Address,Item,Price,User_Info):
        mycursor.execute('SELECT * FROM deliveries')
        data = mycursor.fetchall()
        mycursor.execute("INSERT INTO deliveries (Username,Address,Item,Price,User_Info) VALUES (%s,%s,%s,%s,%s)",(Username,Address,Item,Price,User_Info))
        db.commit()
        return True
    def edit_order(Username,Address,Item,Price,User_Info):
        pass

#print(order.delete_order("Yassa Taiseer","1328 Whitney Terrace","Box",13,"I need this box delivered ASAP"))
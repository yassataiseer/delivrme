import mysql.connector
import os
import requests, json

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
        lat = ""
        lon = ""
        url = 'http://photon.komoot.de/api/?q='
        mycursor.execute('SELECT * FROM deliveries')
        data = mycursor.fetchall()
        resp = requests.get(url=url+Address)
        data = json.loads(resp.text)
        a = data['features'][0]['geometry']['coordinates']
        lat = a[-1]
        lon = a[0]
        mycursor.execute("INSERT INTO deliveries (Username,Address,latitude,longitude,Item,Price,User_Info) VALUES (%s,%s,%s,%s,%s,%s,%s)",(Username,Address,lat,lon,Item,Price,User_Info))
        db.commit()
        return True
    def edit_order(Username,Address,Item,Price,User_Info):
        pass
    def get_order():
        mycursor.execute('SELECT * FROM deliveries')
        data = []
        a = mycursor.fetchall()
        for i in a:
            i = list(i)
            data.append(i)
        return data


#print(order.get_order())

#print(order.add_order("Yassa Taiseer","1328 Whitney Terrace","Box",13,"I need this box delivered ASAP"))
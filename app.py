import mysql.connector
from flask import Flask, render_template,request,session
import os
from decouple import config
import json
from order_manager import order
db =mysql.connector.connect(
    host = config('HOST'),
    user = config('USER'),
    passwd = config('PASSWORD'),
    database = config('DATABASE')
)

app = Flask(__name__)
class School:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

@app.route("/")
def index():
    data1 = order.get_order()
    api_key= config('API_KEY')
    return render_template("map.html", data1=data1,api_key=api_key)

if __name__ == '__main__':
    app.run(port=50000, debug=True) 
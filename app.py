import mysql.connector
from flask import Flask, render_template,request,session
import os
from decouple import config
import json
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
    data1 = [['hv','Happy Valley Elementary',37.9045286,-122.1445772],['ml','1328 Whitney',43.4868212, -79.8437131],['cj',"China",41.41483,82.10606]]
    api_key= config('API_KEY')
    return render_template("map.html", data1=data1,api_key=api_key)

if __name__ == '__main__':
    app.run(port=50000, debug=True) 
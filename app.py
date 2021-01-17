import mysql.connector
from flask import Flask, render_template,request,session
import os
from decouple import config
import json
import requests
from order_manager import order
from user_validator import user
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
app.config['SECRET_KEY'] = 'abc'

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/signup-link")
def signup():
    return render_template("sign_up.html")


@app.route("/login-link")
def login():
    return render_template("login.html")

@app.route("/user-validate", methods = ["POST","GET"])
def validate_user():
    username = request.form['emailer']
    password = request.form['pswrd']
    decision = user.check_user(username,password)
    if decision ==True:
        data1 = order.get_order()
        api_key= config('API_KEY')
        session['Username'] = username
        return render_template("map.html",data1=data1,api_key=api_key)
    else:
        return "invalid password or you need to sign up"
@app.route("/newuser-add",  methods = ["POST","GET"])
def create_user():
    username = request.form['emailer']
    password = request.form['pswrd']
    does_user_exist = user.check_if_user_exists(username)
    print(does_user_exist)
    if does_user_exist == False:
        user.add_user(username,password)
        data1 = order.get_order()
        api_key= config('API_KEY')
        session['Username'] = username
        return render_template("map.html",data1=data1,api_key=api_key)
    else:
        return "Unfortunately a user with this name already exists please pick a new one....."
        

@app.route("/map")
def map_view():
    data1 = order.get_order()
    api_key= config('API_KEY')
    return render_template("map.html", data1=data1,api_key=api_key)

@app.route("/view_orders")
def order_view():
    name = session['Username']
    user_order_info = order.get_order_specific_person(name)
    return render_template("orders.html", data = user_order_info)

if __name__ == '__main__':
    app.run(port=50000, debug=True) 
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
    print(username)
    password = request.form['pswrd']
    does_user_exist = user.check_if_user_exists(username)
    #print(does_user_exist)
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
    print(data1)
    api_key= config('API_KEY')
    return render_template("map.html", data1=data1,api_key=api_key)

@app.route("/view_orders")
def order_view():
    name = session['Username']
    user_order_info = order.get_order_specific_person(name)
    return render_template("orders.html", data = user_order_info)

@app.route("/delete_order", methods=["POST"])
def delete_order():
    final_data = []
    delete_data = request.form['edit']
    delete_data = delete_data.replace("(","")
    delete_data = delete_data.replace(")","")
    delete_data = delete_data.replace("'","")
    print(delete_data)
    delete_data = delete_data.split(',')
    delete_data = list(delete_data)
    first_half = delete_data[0:2]
    secound_half = delete_data[4:7]
    for things in first_half:
        final_data.append(str(things))
    for j in secound_half:
        final_data.append(str(j))
    #final_data.append(delete_data[4:7])
    print(final_data)

    a = order.delete_order(final_data[0].strip(),final_data[1].strip(),final_data[2].strip(),final_data[3].strip(),final_data[4].strip())
    print(final_data[0],final_data[2],int(final_data[3]))
    name = session['Username']
    user_order_info = order.get_order_specific_person(name)
    return render_template("orders.html", data = user_order_info)

@app.route("/deliveryform")
def deliveryform():
    name = session['Username']
    return render_template("deliveryform.html" , name = name)

    
@app.route("/deliverydata", methods = ['POST'])
def deliverydata():
    name = session['Username']
    address = request.form['Address']
    Item = request.form['Item']
    Price = request.form['price']
    info = request.form['info']
    order.add_order(name,address,Item,Price,info)
    user_order_info = order.get_order_specific_person(name)
    return render_template("orders.html", data = user_order_info)
if __name__ == '__main__':
    app.run(port=50000, debug=True) 
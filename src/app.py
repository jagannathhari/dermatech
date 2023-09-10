"""
Author:- Jagannath Hari
File Name:- main.py
Date:- 9/9/2023
Time:- 12:45
"""
from flask import Blueprint
from flask import Flask
import json
from flask_wtf import CSRFProtect
app = Flask(__name__)
app.secret_key = b"this is secret key"

@app.route("/")
def hello_world():
    return "This is a test"

@app.route("/login",methods=["GET","POST"])
def hello_w():
    return "his is a test"

@app.route("/signup",methods = ["POST"])
def hello_worlds():
    return "This is a test"


if __name__ == "__main__":
    print("hello")
    app.run(host="localhost",port=8080,debug=True)






















    

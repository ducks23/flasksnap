#!/usr/bin/env python3
from flask import Flask
from db_info import *
import sys
app = Flask(__name__)

db = DB_info()
db.openFile()
if db.is_connected():
    db.parsefile()

@app.route("/")
def success_route():    
    return "this works" 

@app.route("/error")
def error_route():
    return "a" / 1





app.run(host="0.0.0.0", port=8080)

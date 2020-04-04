#!/usr/bin/env python3
from flask import Flask
from db_info import *
import sys
app = Flask(__name__)
"""
db = DB_info()
db.openFile()
if db.is_connected():
    db.parsefile()

"""



data_folder = Path(f"/var/snap/flasksnap/common/config/")
file_to_open = data_folder / "thecodes.txt"

myNames = None
with open(file_to_open, 'r', encoding="utf-8") as f:
    myNames = [line.split() for line in f]



@app.route("/")
def success_route():    

    return str(myNames)

@app.route("/error")
def error_route():
    return "a" / 1





app.run(host="0.0.0.0", port=5001)

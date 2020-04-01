#!/usr/bin/env python3
from flask import Flask
from db_info import *
import sys
app = Flask(__name__)


db = DB_info()

f = db.openFile()
if db.is_connected():
    db.parsefile(f)




@app.route("/success")
def success_route():
    if db.get_user() != None:
        return db.get_user
    else:
        return "no info :/    "


@app.route("/error")
def error_route():
    return "a" / 1





app.run(host="0.0.0.0", port=5001)

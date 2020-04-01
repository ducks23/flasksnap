#!/usr/bin/env python3
from flask import Flask
from jinja import Environment, FileSystemLoader
from path import Path
from .db_info import DB_info

app = Flask(__name__)


db = DB_info()

f = db.openFile()
db.parsefile(f)


if db.get_user != None:



@app.route("/success")
def success_route():
    if db.get_user != None:
        return db.get_user
    else:
        return "no info :/    "


@app.route("/error")
def error_route():
    return "a" / 1





app.run(host="0.0.0.0", port=5000)

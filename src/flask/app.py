#!/usr/bin/env python3
from flask import Flask
from pathlib import Path
import sys
from db_info import *
from psycopg2 import connect, extensions, sql
import psycopg2


app = Flask(__name__)



@app.route("/dbname")
def info_route():
    a = str(db.get_user() + " " +  db.get_password() + " " +  db.get_host() + " " +  db.get_port())
    return a

@app.route("/close")
def error_route():
    db1 = DB_info()
    data_folder = Path('/var/snap/flasksnap/common/config/')
    file_to_open = data_folder / "text-file.txt"
    info = None
    with open(str(file_to_open), 'r') as f:
        info = [line.split() for line in f]

    for line in info:
        if line[0] == 'DB_USER':
            db1.set_user(line[2][1:-1])
        elif line[0] == 'DB_PASSWORD':
            db1.set_password(line[2][1:-1])
        elif line[0] == 'DB_HOST':
            db1.set_host(line[2][1:-1])
        elif line[0] == 'DB_PORT':
            db1.set_port(line[2][1:-1])
        elif line[0] == 'DB_NAME':
            db1.set_dbname(line[2][1:-1])

    a = str(db1.get_user() + " " +  db1.get_password() + " " +  db1.get_host() + " " +  db1.get_port())
    return a

@app.route("/test")
def tester():
    db1 = DB_info()
    data_folder = Path('/var/snap/flasksnap/common/config/')
    file_to_open = data_folder / "text-file.txt"
    info = None
    with open(str(file_to_open), 'r', encoding="utf-8") as f:
        info = [line.split() for line in f]

    for line in info:
        if line[0] == 'DB_USER':
            db1.set_user(line[1][1:-1])
        elif line[0] == 'DB_PASSWORD':
            db1.set_password(line[1][1:-1])
        elif line[0] == 'DB_HOST':
            db1.set_host(line[1][1:-1])
        elif line[0] == 'DB_PORT':
            db1.set_port(line[1][1:-1])
        elif line[0] == 'DB_NAME':
            db1.set_dbname(line[1][1:-1])

    a = str(db1.get_user() + " " +  db1.get_password() + " " +  db1.get_host() + " " +  db1.get_port())
    return a


if __name__ == '__main__':

    db = DB_info()
    data_folder = Path('/var/snap/flasksnap/common/config/')
    file_to_open = data_folder / "thecodes.txt"
    info = None
    with open(str(file_to_open), 'r', encoding="utf-8") as f:
        info = [line.split() for line in f]

        for line in info:
            if line[0] == 'DB_USER':
                db.set_user(line[1][1:-1])
            elif line[0] == 'DB_PASSWORD':
                db.set_password(line[1][1:-1])
            elif line[0] == 'DB_HOST':
                db.set_host(line[1][1:-1])
            elif line[0] == 'DB_PORT':
                db.set_port(line[1][1:-1])
            elif line[0] == 'DB_NAME':
                db.set_dbname(line[1][1:-1])

    app.run(host="0.0.0.0", port=5001)


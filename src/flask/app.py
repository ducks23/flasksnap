#!/usr/bin/env python3
from flask import Flask
from db_info import *
import sys
from psycopg2 import connect, extensions, sql
import psycopg2


app = Flask(__name__)

db = DB_info()
data_folder = Path(f"/var/snap/flasksnap/common/config/")
file_to_open = data_folder / "thecodes.txt"

info = None


with open(file_to_open, 'r', encoding="utf-8") as f:
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

if db.is_connected():
    try:
        connection = psycopg2.connect(user = db.get_user(),
                                      password = db.get_password,
                                      host = db.get_host(),
                                      port = db.get_port(),
                                      database = "postgres_db")
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)

@app.route("/")
def success_route():    
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")
    return str(connection.get_dsn_parameters())

@app.route("/dbname")
def info_route():
    a = str(db.get_user() + " " +  db.get_password() + " " +  db.get_host() + " " +  db.get_port())
    return a

@app.route("/close")
def error_route():
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        return "PostgreSQL connection is closed"

@app.route("/test")
def tester():
    db1 = DB_info()

    data_folder = Path(f"/var/snap/flasksnap/common/config/")
    file_to_open = data_folder / "text-file.txt"

    info = None


    with open(file_to_open, 'r', encoding="utf-8") as f:
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


@app.route("/other")
def other():
    _db1 = DB_info()

    _data_folder = Path(f"/var/snap/flasksnap/common/config/")
    _file_to_open = _data_folder / "thecodes.txt"

    info = None


    with open(_file_to_open, 'r', encoding="utf-8") as f:
        info = [line.encode('utf-8').strip("'") for line in f]
    return info[0]


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)



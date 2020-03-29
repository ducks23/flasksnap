#!/usr/bin/env python3
from flask import Flask


app = Flask(__name__)



@app.route("/success")
def success_route():
    return "SUCCESS"


@app.route("/error")
def error_route():
    return "a" / 1





app.run(host="0.0.0.0", port=8080)

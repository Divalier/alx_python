#! /usr/bin/python3
"""
    Basics
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home() :
    return "Hello HBNB!" 

if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0",port="5000")
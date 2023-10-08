#! /usr/bin/python3
"""
    basic
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home() :
    return "Hello HBNB!" 

@app.route("/hbnb", strict_slashes=False)
def HBNB() :
    return "HBNB" 

@app.route("/c/<text>", strict_slashes=False)
def C(text) :
    return ("C {}".format(text.replace('_',' ')) )

@app.route("/python/<text>", strict_slashes=False)
def python(text= 'is cool') :
    return ("Python {}".format(text.replace('_',' ')) )

@app.route("/python/", strict_slashes=False)
def python1(text= 'is cool') :
    return ("Python {}".format(text.replace('_',' ')) )


if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0",port="5000")
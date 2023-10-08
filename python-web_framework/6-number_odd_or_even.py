#! /usr/bin/python3
"""
    Basics
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

@app.route("/number/<int:n>", strict_slashes=False)
def number(n) :
        return ("{} is a number".format(n) )

@app.route("/number_template/<int:n>", strict_slashes=False)
def numbers(n) :
     return render_template('5-number.html', num=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def oddOrEven(n) :
     if n%2 == 0:
        return render_template('6-number_odd_or_even.html', num=n, types='even')

     return render_template('6-number_odd_or_even.html', num=n, types='odd')




if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0",port="5000")
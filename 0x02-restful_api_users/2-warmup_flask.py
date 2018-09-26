#!/usr/bin/python3
"""
basic flask application
"""
import os
from flask import Flask

app = Flask(__name__)
host = os.getenv('HBNB_API_HOST')
port = os.getenv('HBNB_API_PORT')


@app.route('/', strict_slashes = False)
def index():
    """ / route method """
    return 'Holberton School'


@app.route('/c', strict_slashes = False)
def c():
    """ /c route method """
    return 'C is fun!'

if __name__ == '__main__':
    app.run(host=host, port=port)

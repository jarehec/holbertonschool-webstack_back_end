#!/usr/bin/python3
"""
basic flask application
"""
from flask import Flask
import os

app = Flask(__name__)
app.url_map.strict_slashes = False
host = os.getenv('HBNB_API_HOST')
port = os.getenv('HBNB_API_PORT')


@app.route('/', methods=['GET'])
def index():
    """ / route method """
    return 'Holberton School'


@app.route('/c', methods=['GET'])
def c():
    """ /c route method """
    return 'C is fun!'

if __name__ == '__main__':
    app.run(host=host, port=port)

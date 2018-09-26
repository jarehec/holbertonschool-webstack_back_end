#!/usr/bin/python3
"""
basic flask application
"""
import os
from flask import Flask, jsonify

app = Flask(__name__)
app.url_map.strict_slashes = False
host = os.getenv('HBNB_API_HOST')
port = os.getenv('HBNB_API_PORT')


@app.route('/hbtn', methods=['GET'])
def index():
    """ /hbtn route method """
    json = {'C': 'is fun', 'Python': 'is cool', 'Sysadmin': 'is hiring'}
    return jsonify(json)

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)

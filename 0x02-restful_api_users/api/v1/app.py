#!/usr/bin/python3
"""
module containing flask app
"""
import os
from flask import Flask, jsonify
from .views import app_views

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

host = os.getenv('HBNB_API_HOST')
port = os.getenv('HBNB_API_PORT')


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(host=host, port=port)

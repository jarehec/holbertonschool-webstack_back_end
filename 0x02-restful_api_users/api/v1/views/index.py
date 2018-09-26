#!/usr/bin/python3
"""
module containing status handler
"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status():
    """ status handler """
    return jsonify({'status': 'OK'})

#!/usr/bin/python3
"""
module containing status handler
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ status handler """
    return jsonify({'status': 'OK'})

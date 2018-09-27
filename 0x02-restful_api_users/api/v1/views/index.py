#!/usr/bin/python3
"""
module containing status handler
"""
from api.v1.views import app_views
from flask import jsonify
from models import db_session
from models.user import User


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ status handler """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ stats handler """
    user_count = len(db_session.query(User).all())
    return jsonify({'users': user_count})

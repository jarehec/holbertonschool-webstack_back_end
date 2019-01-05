#!/usr/bin/python3
"""
module containing status handler
"""
from api.v1.views import app_views
from flask import abort, jsonify
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


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden():
    """ raises 403 error """
    abort(403)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """ raises a 401 error """
    abort(401)

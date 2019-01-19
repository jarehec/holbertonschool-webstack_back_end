#!/usr/bin/python3
"""
session auth view
"""
import os
from api.v1.app import auth
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import db_session
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ login route """
    email = request.form.get('email')
    if type(email) is not str or len(email) == 0:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if type(password) is not str or len(password) == 0:
        return jsonify({"error": "password missing"}), 400
    try:
        user = db_session.query(User).filter(User.email == email).one()
        if not user.is_valid_password(password):
            return jsonify({'error': 'wrong password'}), 401
        user = user.to_dict()
        sess_id = auth.create_session(user['id'])
        out = jsonify(user)
        out.set_cookie(os.getenv('HBNB_YELP_SESSION_NAME'), sess_id)
        return out, 200
    except:
        return jsonify({'error': 'no user found for this email'}), 404


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """ logout route """
    if auth.destroy_session(request) is True:
        return jsonify({}), 200
    abort(404)

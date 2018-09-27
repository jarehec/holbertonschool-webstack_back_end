#!/usr/bin/python3
"""
module containing user handlers
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import db_session
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_users():
    """ shows all users """
    return jsonify({
                     'status': [user.to_dict()
                                for user in db_session.query(User).all()]
                   })


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_one_user(user_id):
    """ gets a user by their id """
    try:
        user = db_session.query(User).filter(User.id == user_id).one()
        return jsonify(user.to_dict())
    except:
        abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def del_one_user(user_id):
    """ removes a user by their id """
    try:
        user = db_session.query(User).filter(User.id == user_id).one()
        db_session.delete(user)
        db_session.commit()
        return jsonify({})
    except:
        abort(404)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """ creates user """
    user = request.get_json()
    if user is None:
        return jsonify({'error': 'Wrong format'}), 400
    if user.get('email') is None:
        return jsonify({'error': 'email missing'}), 400
    if user.get('password') is None:
        return jsonify({'error': 'password missing'}), 400
    try:
        new_user = User()
        new_user.email = user['email']
        new_user.password = user['password']
        new_user.first_name = user.get('first_name')
        new_user.last_name = user.get('last_name')

        db_session.add(new_user)
        db_session.commit()
        return jsonify(new_user.to_dict()), 201
    except Exception as e:
        return jsonify({'error': 'Can\'t create User: ' + e}), 400


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """ updates a user by their id """
    req = request.get_json()
    if req is None:
        return jsonify({'error': 'Wrong format'}), 400
    try:
        user = db_session.query(User).filter(User.id == user_id).one()
        if req.get('first_name') is not None:
            user.first_name = req.get('first_name')
        if req.get('last_name') is not None:
            user.last_name = req.get('last_name')
        db_session.commit()
        return jsonify(user.to_dict())
    except:
        return jsonify({'error': 'Wrong format'}), 400

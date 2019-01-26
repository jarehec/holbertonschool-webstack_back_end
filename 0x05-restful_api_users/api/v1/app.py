#!/usr/bin/python3
"""
module containing flask app
"""
import os
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth
from api.v1.auth.session_exp_auth import SessionExpAuth
from api.v1.auth.session_db_auth import SessionDBAuth
from flask import abort, Flask, jsonify, request
from models import db_session


if os.getenv('HBNB_YELP_AUTH') == 'basic_auth':
    auth = BasicAuth()
elif os.getenv('HBNB_YELP_AUTH') == 'session_auth':
    auth = SessionAuth()
elif os.getenv('HBNB_YELP_AUTH') == 'session_exp_auth':
    auth = SessionExpAuth()
elif os.getenv('HBNB_YELP_AUTH') == 'session_db_auth':
    auth = SessionDBAuth()
else:
    auth = Auth()

from api.v1.views import app_views  # noqa
app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
host = os.getenv('HBNB_API_HOST')
port = os.getenv('HBNB_API_PORT')


@app.before_request
def bfr_req():
    """ function to run before request """
    request.current_user = auth.current_user(request)
    if auth.require_auth(request.path, ['/api/v1/status/',
                                        '/api/v1/unauthorized/',
                                        '/api/v1/forbidden/',
                                        '/api/v1/auth_session/login/'
                                        ]) is False:
        return
    if auth.authorization_header(request) is None and \
       auth.session_cookie(request) is None:
        abort(401)
    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(401)
def user_not_auth(e):
    """ 401 error handler """
    return jsonify({'error': 'Unauthorized'}), 401


@app.errorhandler(403)
def user_no_access(e):
    """ 403 error handler """
    return jsonify({'error': 'Forbidden'}), 403


@app.errorhandler(404)
def page_not_found(e):
    """ 404 page handler """
    return jsonify({'error': 'Not found'}), 404


@app.teardown_appcontext
def teardown(bepis):
    """ close the database connection after request is done """
    db_session.remove()

if __name__ == '__main__':
    app.run(host=host, port=int(port))

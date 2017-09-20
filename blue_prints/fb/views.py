from flask import Blueprint, session, request

# Models
from ..models.model_1 import *

fb = Blueprint('fb', __name__)

@fb.before_request
def before_request():
    # Create db if needed and connect
    initialize_db()

@fb.after_request
def after_request(response):
    db.close()
    return response

# This hook ensures that the connection is closed when we've finished processing the request.
@fb.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

@fb.route('/')
def index():
    if 'user_id' in session:
        return str(session['user_id'])
    return 'You are not logged in.'

@fb.route('/fb_login', methods=['POST'])
def fb_login():
    if 'user_id' not in session:
        user_id = request.json['id']
        try:
            user = User.get(fb_user_id = user_id)
        except User.DoesNotExist:
            user = User.create(fb_user_id = user_id)
        session['user_id'] = user.id
    return str(user.id)


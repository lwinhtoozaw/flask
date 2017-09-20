from flask import Blueprint, render_template, request

# Models
from ..models.model_1 import *

fb = Blueprint('fb', __name__)

@fb.before_request
def before_request():
    # Create db if needed and connect
    initialize_db()

# This hook ensures that the connection is closed when we've finished
# processing the request.
@fb.teardown_request
def _db_close(exc):
    close_db()

@fb.route('/fb_login', methods=['POST'])
def fb_login():
    user_id = request.json['id']
    user = User.select().where(User.fb_user_id == user_id)
    if not user.exists():
        user = User.create(fb_user_id=user_id)
        return user_id + ' has been created'
    else:
        return user_id + ' already exists'


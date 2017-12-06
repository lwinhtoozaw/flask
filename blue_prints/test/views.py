from flask import Blueprint, render_template, session, request

# Models
from ..model_1 import *

test = Blueprint('test', __name__)

@test.before_request
def before_request():
    # Create db if needed and connect
    initialize_db()

# This hook ensures that the connection is closed when we've finished processing the request.
@test.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

# Views
@test.route('/')
def index():
    return 'hah haha ha'
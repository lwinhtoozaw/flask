from flask import Blueprint, render_template

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

# Views
@fb.route('/')
def index():
    return '<h1>This is for facebook</h1>'


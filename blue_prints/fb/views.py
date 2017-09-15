from flask import Blueprint, render_template

fb = Blueprint('fb', __name__)

# Views
@fb.route('/')
def index():
    return '<h1>This is for facebook</h1>'


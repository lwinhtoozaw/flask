from flask import Blueprint, session, request, render_template, redirect, jsonify, url_for
from werkzeug.security import generate_password_hash, check_password_hash

# Models
from ..model_1 import *

# Flask Form
from ..form import LoginForm

import redis

admin = Blueprint('admin', __name__, static_folder='statics', template_folder='templates')

r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)

@admin.before_request
def before_request():
    # Create db if needed and connect
    initialize_db()

@admin.after_request
def after_request(response):
    db.close()
    return response

# This hook ensures that the connection is closed when we've finished processing the request.
@admin.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

@admin.route('/')
def index():
    form = LoginForm()
    css = ['style.css', 'bootstrap.min.css']
    js = ['main.js', 'bootstrap.min.js']
    return render_template('admin/index.html', form = form, css = css, js = js)

@admin.route('/login_go/', methods=['POST'])
def login_go():
    form = LoginForm()
    if form.validate_on_submit():
        errors = []
        try:
            user = User.get(username=form.username.data)
        except User.DoesNotExist:
            errors.append('Invalid Username')
        else:
            if check_password_hash(user.password, form.password.data):
                errors.append('It works')
            else:
                errors.append('Invalid Password')

        if errors:
            form.errors['login'] = errors

    return render_template('error.html', errors = form.errors)
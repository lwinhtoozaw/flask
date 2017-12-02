from flask import Blueprint, session, request, render_template, redirect, jsonify, url_for, abort
from werkzeug.security import generate_password_hash, check_password_hash
from blue_prints import recaptcha

# Models
from ..model_1 import *

import redis

admin = Blueprint('admin', __name__, static_folder='statics', template_folder='templates')

r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)
f = redis.StrictRedis(host = 'localhost', port = 6379, db = 1)

@admin.before_request
def before_request():
    # Create db if needed and connect
    initialize_db()

# This hook ensures that the connection is closed when we've finished processing the request.
@admin.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

def is_loggedin():
    if 'user' not in session:
        return False
    else:
        return True

@admin.route('/')
def index():
    if is_loggedin():
        return redirect(url_for('admin.home'))
    else:
        css = ['style.css', 'bootstrap.min.css']
        js = ['main.js', 'bootstrap.min.js']
        return render_template('admin/index.html', css = css, js = js)

@admin.route('/login_go/', methods=['POST'])
def login_go():
    errors = []
    name = request.form['name']
    password = request.form['password']

    if name == '' or password == '':
        errors.append('Please fill in the form')
    else:
        try:
            admin = Admin.select().where(Admin.name == name).get()
        except Admin.DoesNotExist:
            errors.append('User Not Found')
        else:
            if not check_password_hash(admin.password, password):
                errors.append('Password do not match')
    if not recaptcha.verify():
        errors.append('Recaptcha')
    if not errors:
        session['user'] = admin.id
    return render_template('admin/error.html', errors = errors)

@admin.route('/success/')
def success():
    if is_loggedin():
        return redirect(url_for('admin.home'))
    else:
        return redirect(url_for('admin.index'))

@admin.route('/logout/')
def out():
    session.pop('user', None)
    return redirect(url_for('admin.index'))

@admin.route('/home/')
def home():
    if is_loggedin():
        css = ['bootstrap.min.css','style.css']
        js = ['main.js', 'popper.min.js', 'bootstrap.min.js']
        category = r.smembers('category')
        return render_template('admin/home.html', css = css, js = js, category = category)
    else:
        return redirect(url_for('admin.index'))

@admin.route('/students/')
def students():
    if is_loggedin():
        students = User.select().where(User.block == 0)
        css = ['bootstrap.min.css','style.css']
        js = ['main.js', 'popper.min.js', 'bootstrap.min.js']
        return render_template('admin/students.html', css = css, js = js, students = students)
    else:
        return redirect(url_for('admin.index'))

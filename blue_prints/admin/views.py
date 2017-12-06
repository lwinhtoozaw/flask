from flask import Blueprint, session, request, render_template, redirect, jsonify, url_for, abort
from werkzeug.security import generate_password_hash, check_password_hash
from blue_prints import recaptcha

# Models
from ..model_1 import *

import redis

admin = Blueprint('admin', __name__, static_folder='statics', template_folder='templates')

r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)

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
    css = ['bootstrap.min.css','style.css']
    js = ['main.js', 'popper.min.js', 'bootstrap.min.js']
    category = Category.select()
    return render_template('admin/home.html', css = css, js = js, category = category)


@admin.route('/students/')
def students():
    students = User.select().where(User.block == 0)
    css = ['bootstrap.min.css','style.css']
    js = ['main.js', 'popper.min.js', 'bootstrap.min.js']
    return render_template('admin/students.html', css = css, js = js, students = students)


@admin.route('/category/')
def category():
    categories = Category.select(Category.name)
    css = ['bootstrap.min.css','style.css']
    js = ['main.js', 'popper.min.js', 'bootstrap.min.js']
    return render_template('admin/category.html', css = css, js = js, categories = categories)


#AJAX
@admin.route('/login_go/', methods=['POST'])
def login_go():
    errors = []
    name = request.form['name']
    password = request.form['password']
    url = url_for('admin.success')
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
    return render_template('admin/error.html', errors = errors, url = url)

@admin.route('/add_category/', methods=['POST'])
def add_category():
    errors = []
    name = request.form['name'].lower()
    url = url_for('admin.category')
    if name == '':
        errors.append('Please fill in the form')
    else:
        try:
            category = Category.select().where(Category.name == name).get()
        except Category.DoesNotExist:
            pass
        else:
            errors.append('Exists')
    if not errors:
        Category.insert( name = name).execute()
    return render_template('admin/error.html', errors = errors, url = url)

@admin.route('/add_course/', methods=['POST'])
def add_course():
    errors = []
    name = request.form['name'].lower()
    category = request.form['category']
    keywords = request.form['keys'].lower
    key_list = keywords.split(' ')
    description = request.form['description']

    upload_url = 'main/images/'
    url = url_for('admin.home')
    if name == '' or category == '' or keywords == '' or description == '':
        errors.append('Please fill in the form')
    course = Courses.select().where(Courses.name == name)
    if course.wrapped_count() != 0:
        errors.append('Course name already exists')
    if not errors:
        Courses.insert(name = name, category = category, keywords = key_list, description= description, image = image)
    return render_template('admin/error.html', errors = errors, url = url)

from flask import Blueprint, session, request, render_template, redirect, jsonify, url_for, abort
from werkzeug.security import generate_password_hash, check_password_hash
from blue_prints import recaptcha

import redis

admin = Blueprint('admin', __name__, static_folder='statics', template_folder='templates')

r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)

@admin.route('/')
def index():
    css = ['style.css', 'bootstrap.min.css']
    js = ['main.js', 'bootstrap.min.js']
    return render_template('admin/login.html', css = css, js = js)

@admin.route('/login/', methods = ['POST'])
def login():
    errors = []
    name = request.form['name'].lower()
    password = request.form['password']
    url = url_for('admin.home')
    if name == '' or password == '':
        errors.append('Please fill in the form')
    elif not recaptcha.verify():
        errors.append('Recaptcha')
    else:
        rid = r.hget('user:list', name)
        if rid != None:
            rpassword = r.hget('user:'+rid, 'password')
            if rpassword != 0:
                if not check_password_hash(rpassword, password):
                    errors.append('Wrong Password')
        else:
            errors.append('Wrong Name')
        if not errors:
            session['user'] = rid
    return render_template('admin/error.html', errors=errors, url=url)

        
@admin.route('/home/')
def success():
    return 'YEah'

@admin.route('/logout/')
def logout():
    session.pop('user', None)
    return redirect(url_for('admin.index'))
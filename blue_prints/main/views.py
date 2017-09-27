from flask import Blueprint, render_template, session, request

main = Blueprint('main', __name__, static_folder='statics', template_folder='templates')

# Views
@main.route('/')
def index():
    css = ['main.css']
    js = ['fb_sdk.js', 'fb_login.js', 'main.js']
    return render_template('index.html', js = js, css = css)

@main.route('/a_block', methods = ['POST'])
def a_block():
    return render_template('a_block.html', session = session)
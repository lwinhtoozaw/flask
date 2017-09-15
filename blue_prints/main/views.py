from flask import Blueprint, render_template

main = Blueprint('main', __name__, static_folder='statics', template_folder='templates')

# Views
@main.route('/')
def index():
    return render_template('index.html')
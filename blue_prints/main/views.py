from flask import Blueprint, render_template, session

main = Blueprint('main', __name__, static_folder='statics', template_folder='templates')

# Views
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/a_block', methods = ['POST'])
def a_block():
    return render_template('a_block.html', session = session)
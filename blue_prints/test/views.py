from flask import Blueprint, render_template, session, request

test = Blueprint('test', __name__)

# Views
@test.route('/')
def index():
    return 'hah haha ha'
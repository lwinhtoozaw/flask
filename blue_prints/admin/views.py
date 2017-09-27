from flask import Blueprint, session, request

admin = Blueprint('admin', __name__)

@admin.route('/')
def index():
    return 'lol';


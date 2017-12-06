from flask import Blueprint, render_template, session, request
import redis

r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)
test = Blueprint('test', __name__)

# Views
@test.route('/')
def index():
    text = r.get('user:id')
    return str(text)
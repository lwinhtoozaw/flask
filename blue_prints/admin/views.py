from flask import Blueprint, session, request
import redis

admin = Blueprint('admin', __name__)

r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)

@admin.route('/')
def index():
    return 'lol';


from flask import Blueprint, session, request
import redis

admin = Blueprint('admin', __name__)

r = redis.StrictRedis(host = 'localhost', port = 6379, db=0)

@admin.route('/set/')
def set():
	r.set('too', 'tar')
	return 'True'

@admin.route('/')
def index():
	value = r.keys()
	return str(value)
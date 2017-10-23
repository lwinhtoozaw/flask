from flask import Blueprint, session, request
import redis

admin = Blueprint('admin', __name__)

r = redis.StrictRedis(host = 'localhost', port = 6379, db=0)

@admin.route('/set/')
def set():
	v = r.hset('user', 'age', 23)
	return str(v)

@admin.route('/')
def index():
	value = r.hmget('user', 'age')
	return str(value)
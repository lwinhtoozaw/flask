from flask import Blueprint, session, request
import redis

fb = Blueprint('fb', __name__)

r = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)




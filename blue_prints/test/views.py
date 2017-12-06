from flask import Blueprint, render_template, session, request

from peewee import *

test = Blueprint('test', __name__)

db = PostgresqlDatabase(
    'hermit',
    user = 'postgres',
    password = 'qwerasdf',
)

# Views
@test.route('/')
def index():
    return 'hah haha ha'
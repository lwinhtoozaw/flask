from peewee import *

db = PostgresqlDatabase(
    'hermit',
    user = 'postgres',
    password = 'qwerasdf',
)

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db

class User(BaseModel):
    fb_user_id = CharField()
    email = CharField()
    name = CharField()
    block = IntegerField(default=0)

class Admin(BaseModel):
    name = CharField()
    password = CharField()

class Category(BaseModel):
    name = CharField()

class Courses(BaseModel):
    name = CharField()
    category = CharField()
    keywords = CharField()
    description = TextField()
    image = TextField()


def initialize_db():
    db.connect()
    db.create_tables([User, Admin, Category, Courses], safe = True)

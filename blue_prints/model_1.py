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

def initialize_db():
    db.connect()
    db.create_tables([User], safe = True)

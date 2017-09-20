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

def initialize_db():
    db.connect()
    db.create_tables([User], safe = True)

def close_db():
    if not db.is_closed():
        db.close()

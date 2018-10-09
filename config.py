import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'R4t4t4'
    try:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] 
    except:
        SQLALCHEMY_DATABASE_URI =  'postgresql-globular-12519'
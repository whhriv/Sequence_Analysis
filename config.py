import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'you-might-guess'
   
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.environ.get(basedir, 'app.db')
    #'sqlite:///' + os.path.join(basedir, 'app.db')
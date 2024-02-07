import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')


UNIQUE_ID_LENGTH = 6
CUSTOM_ID_FORM_VALIDATORS = {
    'regexp': '^[a-zA-Z0-9]+$',
    'length': 16
}
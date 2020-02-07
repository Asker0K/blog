import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    # SECRET_KEY settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'yo-will-never-guess'

    # SQLALCHEMY settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # MAIL settings
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    ADMINS = ['askeee886@gmail.com']

    # MAX_COUNT messages on one page(/index)
    POSTS_PER_PAGE = 25

    # translator
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.getenv('MS_TRANSLATOR_KEY')

    # search
    ELASTICSEARCH_URL = os.getenv('ELASTICSEARCH_URL')

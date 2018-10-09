from .common import *

POSTGRES = {
    'user': '######',
    'pw': '######',
    'db': '######',
    'host': '#####',
    'port': '5432',
}

SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
DEBUG = False
HOST_SERVER_URL = '0.0.0.0'
HOST_SERVER_PORT = 80

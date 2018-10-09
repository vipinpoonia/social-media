from .common import *

SQLALCHEMY_ECHO = False
POSTGRES = {
    'user': '',
    'pw': '',
    'db': APP_NAME,
    'host': 'localhost',
    'port': 5432
}
SQLALCHEMY_DATABASE_URI = (
    'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' %
    POSTGRES
)

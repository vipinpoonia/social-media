from os import environ

env = environ['ENV'].lower() if 'ENV' in environ else 'development'

if env == "production":
    from .production import *
elif env == "testing":
    from .testing import *
elif env == "staging":
    from .staging import *
else:
    from .local import *

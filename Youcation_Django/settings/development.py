import os

from .base import *

SECRET_KEY = "$&pk%u%=m25+bg49r_w575!r6-gbya1(ru8d_!#w-t-dlf7%cv"

DEBUG = True

INSTALLED_APPS += [

]

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE += [

]
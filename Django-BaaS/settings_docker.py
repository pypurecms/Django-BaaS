import os

from .settings_base import *

DEBUG = True

ALLOWED_HOSTS = [
    'django-baas.herokuapp.com'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'psql',
        'HOST': os.environ['DATABASE_URL'],
        'PORT': '5432'
    }
}
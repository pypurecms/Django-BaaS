from .settings_base import *

DEBUG = True

ALLOWED_HOSTS = [
    'django-baas.herokuapp.com'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'psql',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
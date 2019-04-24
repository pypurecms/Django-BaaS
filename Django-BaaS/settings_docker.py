from .settings_base import *

DEBUG = True

ALLOWED_HOSTS = [
    'django-baas.herokuapp.com'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'psql',
        'USER': 'root',
        'HOST': 'DATABASE_URL',
        'PORT': '5432'
    }
}
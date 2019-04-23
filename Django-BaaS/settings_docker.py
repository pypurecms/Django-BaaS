from .settings_base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'psql',
        'USER': 'root',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
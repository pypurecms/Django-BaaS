from .settings_base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'psql',
        'USER': 'root',
        'HOST': 'DATABASE_URL',
        'PORT': '5432'
    }
}
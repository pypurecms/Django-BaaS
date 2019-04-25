import os
import dj_database_url
from .settings_base import *

DEBUG = True

ALLOWED_HOSTS = [
    '.herokuapp.com'
]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'psql',
#         'HOST': os.environ['DATABASE_URL'],
#         'PORT': '5432'
#     }
# }

DATABASES['default'] = dj_database_url.parse(os.environ['DATABASE_URL'], conn_max_age=600)

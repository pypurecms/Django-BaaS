import os
import dj_database_url
from .settings_base import *

DEBUG = True

ALLOWED_HOSTS = [
    '.herokuapp.com'
]

DATABASES['default'] = dj_database_url.parse(os.environ['DATABASE_URL'], conn_max_age=600)



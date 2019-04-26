import os
import dj_database_url
import django_heroku
from .settings_base import *

DEBUG = True

# ALLOWED_HOSTS = [
#     '.herokuapp.com'
# ]
#
# DATABASES['default'] = dj_database_url.parse(os.environ['DATABASE_URL'], conn_max_age=600)


# Configure Django App for Heroku.

django_heroku.settings(locals())


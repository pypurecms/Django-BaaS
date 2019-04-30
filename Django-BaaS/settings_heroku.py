import os
import dj_database_url
import django_heroku
from .settings_base import *

DEBUG = True
django_heroku.settings(locals())
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


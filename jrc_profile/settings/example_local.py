import os

from jrc_example.settings.base import BASE_DIR


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mydb',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'myuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, '../collected-static')

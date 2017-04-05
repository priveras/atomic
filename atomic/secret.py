import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u!*v@=xpe@pkaf3ap@&ef*y!g)evz!p7y3lv+mcak%7!@-q@5c'

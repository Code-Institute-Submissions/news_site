from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# PayPal Settings
SITE_URL = [
    'http://127.0.0.1:8000',
    ]
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'nisha3uk@hotmail.com'
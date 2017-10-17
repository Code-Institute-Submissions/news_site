from .base import *

# SECURITY WARNING: don't run with debug turned on in production!

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# PayPal Settings
SITE_URL = [
    'django-news-site.herokuapp.com'
    ]
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/tuux4YjAo2U58peXPSC7/'
PAYPAL_RECEIVER_EMAIL = 'nisha3uk@hotmail.com'

from .base import *
import dj_database_url


# SECURITY WARNING: don't run with debug turned on in production!

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}


# PayPal Settings
SITE_URL = [
    'django-news-site.herokuapp.com'
    ]
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/tuux4YjAo2U58peXPSC7/'
PAYPAL_RECEIVER_EMAIL = 'nisha3uk@hotmail.com'
mysql://b822e4d04ec1e6:c3954cad@eu-cdbr-west-01.cleardb.com/heroku_636d98a1e9d76c9?reconnect=true
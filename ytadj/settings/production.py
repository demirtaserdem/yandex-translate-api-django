from ytadj.settings.base import *

ALLOWED_HOSTS = ['app2.demirtas.biz',]
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{Your Name}',
        'USER': '{Your User}',
        'PASSWORD': '{Your Password}',
        'HOST': 'localhost',
        'PORT': '',
    }
}

#ssl settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True



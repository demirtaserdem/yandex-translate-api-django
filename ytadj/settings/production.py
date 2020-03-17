from ytadj.settings.base import *

ALLOWED_HOSTS = ['app2.demirtas.biz']
DEBUG = False

DATABASES['default']['ENGINE'] = config.get('database', 'DATABASE_ENGINE')
DATABASES['default']['NAME'] = config.get('database', 'DATABASE_NAME')
DATABASES['default']['USER']= config.get('database', 'DATABASE_USER')
DATABASES['default']['PASSWORD'] = config.get('database', 'DATABASE_PASSWORD')
DATABASES['default']['HOST'] = config.get('database', 'DATABASE_HOST')
DATABASES['default']['PORT'] = config.get('database', 'DATABASE_PORT')

#ssl settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True



import os
import sys

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, PROJECT_ROOT)

ADMINS = (
    ('Steven Challis', 'steve@stevechallis.com'),
)

MANAGERS = ADMINS

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'warehouse',
        'USER': os.environ.get('APPSETTING_DB_USER'),
        'PASSWORD': os.environ.get('APPSETTING_DB_PASSWORD'),
        'HOST': os.environ.get('APPSETTING_DB_HOST'),
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'Europe/London'

LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

USE_I18N = True
USE_L10N = False

DATETIME_FORMAT = 'N j, Y, P (T)'

MEDIA_ROOT = ''
MEDIA_URL = ''

if os.environ.get('APPSETTING_LOCAL_STATIC') == 'true':
    STATIC_ROOT = 'static/'
    STATIC_URL = '/static/'
else:
    STATIC_ROOT = 'D:/home/site/wwwroot/static'
    STATIC_URL = 'https://portalvhds52l58tfthh6wl.blob.core.windows.net/staticfiles/'
    STATICFILES_STORAGE = 'azure_storage.storage.AzureStorage'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


SECRET_KEY = '((@b3f+s!o8^r$wb$p8@+&8k@&y*3o7sy3dp4xk+45=$e2996x'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'warehouse.urls'

TEMPLATE_DIRS = ()

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'debug_toolbar',
    'reporting',
)

#INTERNAL_IPS = ('127.0.0.1', )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'verbose': {
            'format': '[%(levelname)s %(threadName)s %(asctime)s %(module)s] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'stream': sys.stdout
        },
    },
    'loggers': {
        'reporting': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

BORK_URL = 'http://api.zonza.tv:8080/v0/'
BORK_AUTH = {
    'Bork-Token': os.environ.get('APPSETTING_BORK_TOKEN'),
    'Bork-Username': os.environ.get('APPSETTING_BORK_USERNAME'),
}

AZURE_STORAGE = {
    'ACCOUNT_NAME': os.environ.get('APPSETTING_STORAGE_ACCOUNT_NAME'),
    'ACCOUNT_KEY': os.environ.get('APPSETTING_STORAGE_ACCOUNT_KEY'),
    'CONTAINER': 'staticfiles',
    'STATIC_CONTAINER': 'static',
    'CDN_HOST': None,
    'USE_SSL': False,
}

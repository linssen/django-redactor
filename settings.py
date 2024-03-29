# Django settings for redactor_test project.
import os
from django.conf.global_settings import *

#==============================================================================
# General project settings
#==============================================================================

SITE_ID = 1

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Erskine Design', 'dev@erskinedesign.com'),
)
MANAGERS = ADMINS

SECRET_KEY = ',]2aKKW6>=OXOE.ND}3Cgc{n*Z#.^/uS6Z7Brs~:b^JQ<#H>Eg'

ROOT_URLCONF = 'redactor_test.urls'

CURDIR = os.path.dirname(__file__)

#==============================================================================
# Localisation settings
#==============================================================================

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en-gb'
USE_I19N = True
USE_L10N = True

#==============================================================================
# Media settings
#==============================================================================

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MEDIA_ROOT = CURDIR + '/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = CURDIR + '/static_collected/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    CURDIR + '/static/',
)

#==============================================================================
# Template settings
#==============================================================================

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
    'redactor_test.context_processors.site',
)

TEMPLATE_DIRS = (
    CURDIR + '/templates/',
)

#==============================================================================
# Middleware settings
#==============================================================================

MIDDLEWARE_CLASSES = (
    'annoying.middlewares.StaticServe',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

#==============================================================================
# Base logging config
#==============================================================================

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#==============================================================================
# Application settings
#==============================================================================

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Third-party apps
    'south',
    'debug_toolbar',
    'sorl.thumbnail',
    'django_extensions',
    'markitup',
    'compressor',
    'typogrify',
    # Project-specific apps
    'redactor_test.blog',
    'redactor_test.redactor',
)

MARKITUP_SET = 'plugins/markitup/sets/clientproof'
MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': False})

# For the debug toolbar
INTERNAL_IPS = (
    '127.0.0.1',
    '194.50.121.65',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

# Do not edit below this line
try:
    from local_settings import *
except:
    pass

"""
Django settings for forthebirds project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(SETTINGS_DIR, '..')

from local_settings import (DEBUG, SECRET_KEY, DATABASES,
                            STATIC_ROOT, MEDIA_ROOT)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'markdown_deux',
    'taggit',

    'website',
    'utils',
    'birds',
    'creations',
    'waystohelp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'forthebirds.urls'

WSGI_APPLICATION = 'forthebirds.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

# Media files (User-uploaded files)
MEDIA_URL = '/media/'

# For request object in templates
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

# Needed so overridden admin templates take precedence
TEMPLATE_DIRS = (
    PROJECT_DIR + '/website/templates/',
)

# Authentication
LOGIN_URL = 'login_url'
LOGIN_REDIRECT_URL = 'home_url'

# Constants
MARKDOWN_PROMPT = (
    'Use Markdown syntax for italics, bullets, etc. See '
    '<a href="http://www.darkcoding.net/software/markdown-quick-reference">'
    'a quick reference</a>, '
    '<a href="http://www.markdowntutorial.com/">a tutorial</a>, '
    'or practice <a href="http://dillinger.io/">here</a>. '
)

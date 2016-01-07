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


# Note: I hard-coded the site domain in local_settings in order to
# use it in the podcast feed. For some reason, while Django does prefix
# the feed-wide url and feed item page urls with the domain name,
# it is does not add this prefix to the enclosure mp3 url. Since
# iTunes requires the domain name in the enclosure url, I need to add
# it myself. And since the request object is not accessible when
# extending a Feed object, I have it in this settings file.
#
# I opted not to use the Sites framework for this since it does not
# seem to be the intention of the Sites framework.
#
from local_settings import (DEBUG, SECRET_KEY, DATABASES,
                            SITE_DOMAIN, STATIC_ROOT, MEDIA_ROOT,
                            PRIVATE_MEDIA_ROOT, PRIVATE_MEDIA_SERVER)

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

    'jquery',
    'markdown_deux',
    'private_media',
    'sorl.thumbnail',
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Media files (User-uploaded files)
MEDIA_URL = '/media/'

# Private media files
PRIVATE_MEDIA_URL = '/private-media/'

# For request object in templates
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

# Needed so overridden admin templates take precedence
TEMPLATE_DIRS = (
    BASE_DIR + '/website/templates/',
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

"""
Django settings for forthebirds project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Local configuration

# Note: I hard-coded the site domain in localsettings to use it in
# the podcast feed. For some reason, while Django does prefix
# the feed-wide url and feed item page urls with the domain name,
# it is does not add this prefix to the enclosure mp3 url. Since
# iTunes requires the domain name in the enclosure url, I need to add
# it myself. And since the request object is not accessible when
# extending a Feed object, I have it in this settings file.
# I opted not to use the Sites framework for this since it does not
# seem to be the intention of the Sites framework.

from localsettings import (
    DEBUG, SECRET_KEY, DATABASES, SITE_DOMAIN, OLD_SITE_DOMAIN,
    ITUNES_SUBSCRIBE_LINK, GOOGLE_ANALYTICS_ID, PERMANENT_REDIRECTS,
    STATIC_URL, MEDIA_URL, STATIC_ROOT, MEDIA_ROOT, PATREON_LINK,)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Security

ALLOWED_HOSTS = ['*']


# Administration

ADMINS = [('Katherine Erickson', 'katherine.erickson@gmail.com')]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'jquery',
    'sorl.thumbnail',
    'taggit',

    'website',
    'birds',
    'creations',
    'waystohelp',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'forthebirds.urls'

WSGI_APPLICATION = 'forthebirds.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,

        # Needed so overrideen admin templates take precedence
        'DIRS': [BASE_DIR + '/website/templates/'],

        'OPTIONS': {
            # Needed to provide request object in templates
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'forthebirds.context_processors.google_analytics',
                'forthebirds.context_processors.static_asset_hashes',
            ],
        },
    },
]


# Login

LOGIN_URL = 'login_url'
LOGIN_REDIRECT_URL = '/'


# Miscellany
CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/radio/program-count$'

MARKDOWN_PROMPT = (
    'Use Markdown syntax for italics, bullets, etc. See '
    '<a href="https://daringfireball.net/projects/markdown/syntax">'
    'a quick reference</a>, '
    '<a href="http://www.markdowntutorial.com/">a tutorial</a>, '
    'or practice <a href="http://dillinger.io/">here</a>. '
)

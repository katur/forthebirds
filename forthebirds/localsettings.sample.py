DEBUG = True


SITE_DOMAIN = 'https://www.lauraerickson.com'
OLD_SITE_DOMAIN = 'http://old.lauraerickson.com'


SECRET_KEY = '<your secret key>'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': '<your mysql user>',
        'PASSWORD': '<your mysql user password>',
        'HOST': '<the database host>',
        'PORT': '<the database port>',
        'NAME': '<the database name>',
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'


GOOGLE_ANALYTICS_ID = '<add if you have google analytics>'

FLICKR_USER_ID = '<your flickr user>'
FLICKR_KEY = '<your flickr api key>'
FLICKR_SECRET = '<your flickr secret key>'

ITUNES_SUBSCRIBE_LINK = (
    'https://geo.itunes.apple.com/us/podcast/'
    'laura-ericksons-for-the-birds/id655880335?mt=2'
)

PATREON_LINK = 'https://www.patreon.com/lauraerickson'

PERMANENT_REDIRECTS = []

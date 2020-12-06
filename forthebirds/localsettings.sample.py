DEBUG = True

SITE_DOMAIN = 'http://localhost:8000'
OLD_SITE_DOMAIN = 'https://old.lauraerickson.com'

SECRET_KEY = '<your secret key>'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': '<your mysql user>',
        'PASSWORD': '<your mysql user password>',
        'HOST': '<the database host>',
        'PORT': 3306,
        'NAME': '<the database name>',
    }
}

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

MEDIA_ROOT = 'mediafiles'
MEDIA_URL = '/media/'

GOOGLE_ANALYTICS_ID = '<add if you have google analytics>'

FLICKR_USER_ID = '<your flickr user>'
FLICKR_KEY = '<your flickr api key>'
FLICKR_SECRET = '<your flickr secret key>'

ITUNES_SUBSCRIBE_LINK = (
    'https://geo.itunes.apple.com/us/podcast/'
    'laura-ericksons-for-the-birds/id655880335?mt=2'
)

PATREON_LINK = 'https://www.patreon.com/lauraerickson'

PERMANENT_REDIRECTS = [
    ('index.html', '/'),
    ('AboutLaura.html', '/about-laura'),
    ('Calendar.html', '/about-laura'),

    ('Radio/Podcasts/FTB.html', '/radio/'),
    ('Radio/Podcasts/FTB.xml', '/radio/feed.xml'),
    ('Radio/FortheBirds.html', '/radio/'),

    ('bird/Species/Owls/HarryPotter/HarryPotter.html',
     '/page/owls-of-harry-potter/'),
    ('bird/Species/Owls/HarryPotter/Hedwig.html',
     '/page/owls-of-harry-potter-book-7-spoilers/'),

    ('bird/Species/Directory.html', '/birds/'),

    ('101.html', '/book/101-ways-to-help-birds/'),
    # ('101/Intro.html', '/ways-to-help/'),
    # ('101/02-House/006-windows.html', '/way-to-help/6/'),

    ('Stories/StoryIndex.html', '/miscellany/'),
]

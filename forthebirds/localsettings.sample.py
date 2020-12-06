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
    (r'^index.html', '/'),
    (r'^AboutLaura.html', '/about-laura'),
    (r'^Calendar.html', '/about-laura'),

    (r'^Radio/FortheBirds.html', '/radio/'),
    (r'^Radio/Podcasts/FTB.html', '/radio/'),
    (r'^Radio/Podcasts/FTB.xml', '/radio/feed.xml'),

    (r'^bird/Species/Owls/HarryPotter/HarryPotter.html',
     '/page/owls-of-harry-potter/'),
    (r'^bird/Species/Owls/HarryPotter/Hedwig.html',
     '/page/owls-of-harry-potter-book-7-spoilers/'),

    (r'^bird/Species/Directory.html', '/birds/'),

    (r'^101.html', '/book/101-ways-to-help-birds/'),
    # ('101/Intro.html', '/help-birds/'),
    # ('101/02-House/006-windows.html', '/help-birds/6/'),

    (r'^Stories/StoryIndex.html', '/miscellany/'),
    (r'^Radio/Podcasts/Archives/PaulWellstone.html', '/page/lauras-tribute-paul-wellstone/'),
    (r'^Radio/Podcasts/Archives/FredRogers.html', '/page/lauras-tribute-mr-rogers/'),

    # Outdated bird species names
    (r'^bird/nutmeg-mannikin/', '/bird/scaly-breasted-munia/'),
    (r'^bird/orange-bishop/', '/bird/northern-red-bishop/'),
    (r'^bird/common-moorhen/', '/bird/eurasian-moorhen/'),
    (r'^bird/shy-albatross/', '/bird/white-capped-albatross/'),
]

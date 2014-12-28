from django.conf.urls import patterns, url


urlpatterns = patterns(
    'creations.views',
    url(r'^radio$', 'radio', name='radio_url'),
    url(r'^writing$', 'writing', name='writing_url'),
    url(r'^article/(?P<id>.+)$', 'article', name='article_url'),
    url(r'^miscellany$', 'miscellany', name='miscellany_url'),
    url(r'^research-categories', 'research_categories',
        name='research_categories_url'),
    url(r'^research-category/(?P<id>.+)$', 'research_category',
        name='research_category_url'),
    url(r'^research/(?P<id>.+)$', 'research', name='research_url'),
)

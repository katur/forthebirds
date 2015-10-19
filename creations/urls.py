from django.conf.urls import patterns, url


urlpatterns = patterns(
    'creations.views',
    url(r'^radio$', 'radio', name='radio_url'),
    url(r'^radio/(?P<id>.+)$', 'radio_program', name='radio_program_url'),
    url(r'^writing$', 'writing', name='writing_url'),
    url(r'^book/(?P<id>.+)$', 'book', name='book_url'),
    url(r'^article/(?P<id>.+)$', 'article', name='article_url'),
    url(r'^speaking$', 'speaking', name='speaking_url'),
    url(r'^speaking/(?P<id>.+)$', 'speaking_program',
        name='speaking_program_url'),
    url(r'^page/(?P<slug>.+)$', 'webpage', name='webpage_url'),
    url(r'^miscellany$', 'miscellany', name='miscellany_url'),
    url(r'^all-research', 'all_research', name='all_research_url'),
    url(r'^research-category/(?P<id>.+)$', 'research_category',
        name='research_category_url'),
    url(r'^research/(?P<id>.+)$', 'research', name='research_url'),
)

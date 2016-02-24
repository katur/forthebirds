import flickrapi

from forthebirds.local_settings import (FLICKR_KEY, FLICKR_SECRET,
                                        FLICKR_USER_ID)

DEFAULT_PER_PAGE = 10


def connect_to_flickr(format='parsed-json'):
    """
    Connect to Flickr.

    Returns the FlickrAPI connection object.
    """
    return flickrapi.FlickrAPI(FLICKR_KEY, FLICKR_SECRET, format=format)


def search_flickr(tags, per_page=DEFAULT_PER_PAGE, media='all'):
    """
    Search on Flickr for photos matching all tags in the list `tags`.

    Limited to photos by user with FLICKR_USER_ID.

    Optionally define per_page to define how many photos per page
    (defaults to DEFAULT_PER_PAGE).

    Optionally pass media='photos' or media='videos' to limit to just
    that media type.
    """
    flickr = connect_to_flickr()

    return flickr.photos.search(
        user_id=FLICKR_USER_ID,
        tag_mode='all',
        tags=','.join(tags),
        per_page=per_page,
        media=media)

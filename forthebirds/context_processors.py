import os
import json
from django.conf import settings


def google_analytics(request):
    return {'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID}


def static_asset_hashes(request):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    hash_file = '{}/static_asset_hashes.json'.format(dir_path)

    try:
        with open(hash_file) as f:
            hashes = json.load(f)

    except Exception:
        hashes = {}

    return {'static_asset_hashes': hashes}

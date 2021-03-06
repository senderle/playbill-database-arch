with open('schema.py', 'r') as f:
    exec(f.read())

ephemeralRecord = {
    'public_methods': ['GET'],
    'public_item_methods': ['GET'],
    'item_title' : 'record',
    'allowed_roles': ['superuser', 'admin', 'user'],
    'schema': schema
}

accounts = {
    'item_title' : 'account',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'userid',
    },

    # We also disable endpoint caching as we don't want client apps to
    # cache account data.
    'cache_control': '',
    'cache_expires': 0,
    'allowed_roles': ['admin'],
    'schema': accountschema
}

geocodes = {
    'public_methods': ['GET'],
    'public_item_methods': ['GET'],
    'item_title' : 'geocode',
    'allowed_roles': ['superuser', 'admin', 'user'],
    'schema': geoschema
}

DOMAIN = {
    'ephemeralRecord': ephemeralRecord,
    'accounts': accounts,
    'geocodes': geocodes
    }

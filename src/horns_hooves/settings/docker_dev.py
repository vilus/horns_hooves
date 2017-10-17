import sys
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGGING['handlers']['console'] = {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'stream': sys.stdout,
                                  'formatter': 'verbose'}
LOGGING['loggers']['django']['handlers'] = ['console']
LOGGING['loggers']['django']['level'] = 'DEBUG'
LOGGING['loggers']['dev']['handlers'] = ['console']
LOGGING['loggers']['dev']['level'] = 'DEBUG'

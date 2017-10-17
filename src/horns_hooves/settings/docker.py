import sys
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    }
}

LOGGING['handlers']['console'] = {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'stream': sys.stdout,
                                  'formatter': 'verbose'}
LOGGING['loggers']['django']['handlers'] = ['console']
LOGGING['loggers']['django']['level'] = 'DEBUG'
LOGGING['loggers']['dev']['handlers'] = ['console']
LOGGING['loggers']['dev']['level'] = 'DEBUG'

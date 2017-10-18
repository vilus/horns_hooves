import os
from tempfile import gettempdir
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(gettempdir(), 'dock_dev.sqlite3'),
    }
}

LOGGING['loggers']['django']['level'] = 'INFO'
LOGGING['loggers']['dev']['level'] = 'DEBUG'

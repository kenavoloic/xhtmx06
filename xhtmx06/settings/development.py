from .base import *
from dotenv import load_dotenv
import os

load_dotenv('.env.development')

DEBUG = True

# Base de données SQLite pour le développement
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Django Debug Toolbar
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

# Hosts autorisés
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

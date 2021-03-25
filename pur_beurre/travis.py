"""Django settings for Projet8 project in Travis."""

from .base import *

SECRET_KEY = os.getenv('SECRET_KEY', 'a-very-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'purbeurredb',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '/tmp/',
        'PORT': '',
    }
}
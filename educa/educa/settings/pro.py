from .base import *
DEBUG = False
ADMINS = (
    ('rajasmit', 'rajasmitmondal@yahoo.com'),
)
ALLOWED_HOSTS = ['.educaproject.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '*****',
    }
}

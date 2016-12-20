
from os.path import dirname, join

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(dirname(__file__), 'db.sqlite3'),
    }
}
INSTALLED_APPS = (
    'libs',
)

SECRET_KEY = "ABCDEFG"


from os.path import dirname, join

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(dirname(__file__), 'db.sqlite3'),
    }
}
INSTALLED_APPS = (
    'libs',
    'django_jenkins'
)

PROJECT_APPS = ["libs"]

JENKINS_TASKS = (
    "django_jenkins.tasks.run_pylint",
    "django_jenkins.tasks.run_pep8",
    "django_jenkins.tasks.run_flake8",
    "django_jenkins.tasks.run_sloccount",
)

SECRET_KEY = "ABCDEFG"

"""
Django settings for ncsUpload project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = '&puhmjacov-904el1pl-eap+h&_$^5@1)hq7jck-)xq^anw0q%'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ncsUpload.urls'

WSGI_APPLICATION = 'ncsUpload.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


TEMPLATE_DIRS = (
    os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), \
        'ncsUpload/templates')
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",)
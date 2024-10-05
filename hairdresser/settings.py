"""
Django settings for the hairdresser project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config  # Import decouple to read from .env
import os
import dj_database_url  # Import for database URL configuration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Media file settings
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Static file settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Directory for additional static files
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Directory for collected static files

# WhiteNoise settings for serving static files in production
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Security settings
SECRET_KEY = config('SECRET_KEY')  # Load the secret key from .env
DEBUG = config('DEBUG', default=False, cast=bool)  # Load debug mode from .env

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], 
                       cast=lambda v: [s.strip() for s in v.split(',')])  # Allow hosts

# Redirect after successful login
LOGIN_REDIRECT_URL = 'custom_login_redirect'  # After login, redirect to profile

# Redirect after logout
LOGOUT_REDIRECT_URL = 'home'  # After logout, redirect to home page

# URL for login page
LOGIN_URL = 'login'

# CSRF and session cookie security for production
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=True, cast=bool)  # Enable in production
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=True, cast=bool)  # Enable in production

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'clients',  # Clients app
    'hairdressers',  # Hairdressers app
    'appointments',  # Appointments app
    'reviews',  # Reviews app
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Middleware for static file handling in production
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "hairdresser.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ensure that the templates folder exists
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'hairdresser.context_processors.user_role',  # Custom context processor
            ],
        },
    },
]

WSGI_APPLICATION = "hairdresser.wsgi.application"

# Database configuration
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')  # Load database URL from .env
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True  # Enable internationalization
USE_TZ = True  # Enable timezone support

# Static files (CSS, JavaScript, Images) settings
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Directory for collected static files
STATICFILES_DIRS = [BASE_DIR / 'static']  # Additional static files directories

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Directory for media files

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"  # Set the default primary key type

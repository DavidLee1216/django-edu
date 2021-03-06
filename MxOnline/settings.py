"""
Django settings for MxOnline project.
#_*_ encoding:utf-8 _*_

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import os.path

import sys
import os
from imp import reload
from django.views.generic import TemplateView#process static file
from decouple import config, Csv
import dj_database_url

import logging.config
from django.utils.log import DEFAULT_LOGGING


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))#insert at 0 position
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 's%a+mg5+&k-ge(_!7q2mjk0+zc7*1-#$h9j+_$e*9+8489td5('
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#if debug==false(in production mode), django will not looking for static files in staticfiles_dir,django server will not be static file's agent

# ALLOWED_HOSTS = ['*']


# Application definition
AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'courses',
    'organization',
    'operation',
    'xadmin',
    'crispy_forms',
    'captcha',
    'pure_pagination',
    'contactus',
    'DjangoUeditor',
    'cart_payment',
    'storages'
]

AUTH_USER_MODEL = "users.UserProfile"

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MxOnline.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
		        'django.template.context_processors.media',
                'utils.base_context_processors.base_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'MxOnline.wsgi.application'

LOGIN_REDIRECT_URL='/users/info/'
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': "mxonline",
#         'USER': "root",
#         'PASSWORD': "",
#         'HOST': "localhost"

#     }
# }


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# STATIC_ROOT = ''


# STATIC_ROOT = '/static/'

# STATICFILES_DIRS = ( os.path.join('static'), )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
#     '/static/',
# ]
STATICFILES_DIRS=(os.path.join(BASE_DIR, 'static'),
                  )

STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
EMAIL_FROM=config('EMAIL_FROM')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
ADMIN_EMAIL=config('ADMIN_EMAIL')

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


#production mode
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CONTACT_US_EMAIL=config('CONTACT_US_EMAIL')

########## paytm ##########


PAYTM_MERCHANT_KEY = config('PAYTM_MERCHANT_KEY')
PAYTM_MERCHANT_ID = config('PAYTM_MERCHANT_ID')
PAYTM_WEBSITE = config('PAYTM_WEBSITE')
HOST_URL = config('HOST_URL')
PAYTM_CALLBACK_URL = "/cart_payment/response/"
PAYTM_INDUSTRY_TYPE_ID=config('PAYTM_INDUSTRY_TYPE_ID')
PAYTM_CHANNEL_ID=config('PAYTM_CHANNEL_ID')
PAYTM_SERVER_URL=config('PAYTM_SERVER_URL')
PAYTM_TRANSACTION_STATUS_URL=config('PAYTM_TRANSACTION_STATUS_URL')



LIVE_ONLINE_COURSE = config('LIVE_ONLINE_COURSE')

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'MxOnline.storage_backends.MediaStorage'
MEDIAFILES_LOCATION = 'media'

MEDIA_URL ='https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
MEDIA_ROOT = MEDIA_URL
LOGLEVEL = config('LOG_LEVEL').upper()
DJANGO_LOG_LEVEL=config('DJANGO_LOG_LEVEL').upper()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'file': {
            'level': LOGLEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': config('LOG_FILE_NAME'),
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': DJANGO_LOG_LEVEL,
            'propagate': True,
        },
        'users': {
            'handlers': ['console','file'],
            'level': LOGLEVEL,
            'propagate': True,
    },
        'cart_payment': {
            'handlers': ['console','file'],
            'level': LOGLEVEL,
            'propagate': True,
    },
        'courses': {
            'handlers': ['console','file'],
            'level': LOGLEVEL,
            'propagate': True,
    },
        'operation': {
            'handlers': ['console','file'],
            'level': LOGLEVEL,
            'propagate': True,
    },
        'organization': {
            'handlers': ['console','file'],
            'level': LOGLEVEL,
            'propagate': True,
    },
        'utils': {
            'handlers': ['console','file'],
            'level': LOGLEVEL,
            'propagate': True,
    },
    },
}



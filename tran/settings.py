#coding=utf-8
"""
Django settings for tran_2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a!sy^q+nf^qx)^a!0p7z&d+)q8zvye#bpz^vfjq--!sl46^-tb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'project',
    'members',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'tran.urls'

WSGI_APPLICATION = 'tran.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-CN'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, '')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    #'BriefWeb.processors.get_side_panel',  # 模板全局变量加器，自定义
    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.media",
)

# 修改上传时文件在内存中可以存放的最大size为10m
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760
# sae的本地文件系统是只读的，修改django的file storage backend为Storage
DEFAULT_FILE_STORAGE = 'sae.ext.django.storage.backend.Storage'
# 使用media这个bucket
STORAGE_BUCKET_NAME = 'media'
# ref: https://docs.djangoproject.com/en/dev/topics/files/


try:
    from product import *
except ImportError:
    pass

try:
    from local import *
except ImportError:
    pass
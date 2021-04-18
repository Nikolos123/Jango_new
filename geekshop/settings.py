"""
Django settings for geekshop project.

Generated by 'django-admin startproject' using Django 2.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm0y-s2nhj(*ba33vbhlgg#b10i4uv0$qd*^-07(bw*f&voxtdw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my app
    'mainapp',
    'authapp',
    'basketapp',
    'adminapp',
    'ordersapp',
    'social_django',

    'debug_toolbar',
    'template_profiler_panel',


]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # 'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.vk.VKOAuth2',
    # 'social_core.backends.facebook.FacebookOAuth2',
    # 'social_core.backends.github.GithubOAuth2',
    # 'social_core.backends.apple.AppleIdAuth',
)
# Загружаем секреты из файла
SOCIAL_SECRETS_FILE = "geekshop/social_auth.json"
SOCIAL = {}
if os.path.exists(SOCIAL_SECRETS_FILE):
    with open(SOCIAL_SECRETS_FILE, 'r')as f:
        SOCIAL = json.load(f)

SOCIAL_AUTH_VK_OAUTH2_KEY = SOCIAL.get('SOCIAL_AUTH_VK_OAUTH2_KEY', "")
SOCIAL_AUTH_VK_OAUTH2_SECRET = SOCIAL.get('SOCIAL_AUTH_VK_OAUTH2_SECRET', "")
# SOCIAL_AITH_VK_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = SOCIAL.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY', "")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = SOCIAL.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET', "")
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']

SOCIAL_AUTH_FACEBOOK_OAUTH2_KEY = SOCIAL.get('SOCIAL_AUTH_FACEBOOK_OAUTH2_KEY', "")
SOCIAL_AUTH_FACEBOOK_OAUTH2_SECRET = SOCIAL.get('SOCIAL_AUTH_FACEBOOK_OAUTH2_SECRET', "")
SOCIAL_AUTH_FACEBOOK_OAUTH2_SCOPE = ['email']

SOCIAL_AUTH_GITHUB_OAUTH2_KEY = SOCIAL.get('SOCIAL_AUTH_GITHUB_OAUTH2_KEY', "")
SOCIAL_AUTH_GITHUB_OAUTH2_SECRET = SOCIAL.get('SOCIAL_AUTH_GITHUB_OAUTH2_SECRET', "")
SOCIAL_AUTH_GITHUB_OAUTH2_SCOPE = ['email']

SOCIAL_AUTH_URL_NAMESPACE = 'social'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'geekshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # Добавил эту строку
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'geekshop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABESE_SECRETS_FILE = "geekshop/database.json"
# DATABESE = {}
# if os.path.exists(DATABESE_SECRETS_FILE):
#     with open(DATABESE_SECRETS_FILE, 'r')as f:
#         DATABESE = json.load(f)
#
# DATABASES = {
#     'default': {
#         'ENGINE': DATABESE.get('ENGINE', ""),
#         'NAME': DATABESE.get('NAME', ""),
#         'USER': DATABESE.get('USER', "")
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static')
# )

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

AUTH_USER_MODEL = 'authapp.User'
LOGIN_URL = '/auth/login/'

DOMAIN_NAME = 'http://localhost:8000'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

LOGIN_PASSWOR_HOST = "geekshop/auto.json"
LOGIN_PASSWOR = {}
if os.path.exists(LOGIN_PASSWOR_HOST):
    with open(LOGIN_PASSWOR_HOST, 'r')as f:
        LOGIN_PASSWOR = json.load(f)

EMAIL_HOST = LOGIN_PASSWOR.get('EMAIL_HOST', '')
EMAIL_HOST_USER = LOGIN_PASSWOR.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = LOGIN_PASSWOR.get('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = LOGIN_PASSWOR.get('EMAIL_PORT', '')
EMAIL_USE_TLS = LOGIN_PASSWOR.get('EMAIL_USE_TLS', '')

LOGIN_REDIRECT_URL = "/"
LOGIN_ERROR_URL = "/"

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.create_user',
    'authapp.pipelines.save_user_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

if DEBUG:
    def show_toolbar(request):
        return True


    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
        'template_profiler_panel.panels.template.TemplateProfilerPanel',
    ]

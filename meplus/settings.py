import os

from pathlib import Path
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-woi%1a89ox77klprfn*a$y%=s8+hq*k)t&u&7&ti&m&@xj=k1_'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'match.apps.MatchConfig',
    # 'accounts.apps.AccountsConfig',
    'operation.apps.OperationConfig',
    # 'credicards.apps.CreditcardsConfig',

    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'django_bootstrap5',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meplus.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'meplus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'meplus',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{"min_length":6},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MESSAGE_TAGS = {
    messages.ERROR: 'alert alert-denger',
    messages.WARNING: 'alert alert-warning',
    messages.SUCCESS: 'alert alert-success',
    messages.INFO: 'alert alert-info',
}

# AUTH_USER_MODEL ='accounts.MeplusUser'

# ロギング設定
LOGGING = {
    'version': 1, #1固定
    'disable_existing_loggers': False,

    # ロガーの設定
    'Loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers':['console'],
            'level':'INFO',
        },
        # fearアプリケーションが利用するロガー
        'fear': {
            'handlers':['console'],
            'level':'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev'
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathtime)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        }
    }
}


# # django-allauthで利用するdjango.contrib.sitesを使うためにサイト識別用IDを設定
# SITE_ID = 1
#
# AUTHENTICATION_BACKENDS = (
#     # 一般ユーザー用(メールアドレス認証)
#     'allauth.accounts.auth_backends.AuthenticationBackend',
#     # 管理サイト用(メールアドレス認証)
#     'django.contrib.auth.backends.ModelBackend'
# )
# # メールアドレス認証に変更する設定
# ACCOUNT_AUTHENTICATION_METHOD ='email'
# ACCOUNT_USERNAME_REQUIRED = False
#
# # サインアップにメールアドレス確認をはさむように設定
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_EMAIL_REQUIRED = True
#
# # # ログイン/ログアウト後の遷移先を設定
# # LOGIN_REDIRECT_URL = 'match:home'
# # ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
#
# # ログアウトリンク一発でログアウトする設定
# ACCOUNT_LOGOUT_ON_GET = True
#
# # django-allauthが送信するメール件名に自動付与される接頭辞をブランクにする設定
# ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
#
# # デフォルトのメール送信先の設定
# DEFAULT_FROM_EMAIL = os.environ.get('FROM_EMAIL')

MEDIA_URL = '/media/'

# 画像を保存する先の指定
MEDIA＿ROOT = os.path.join(BASE_DIR, 'media')

# PASSWORD_HASHERS = [
#     "django.contrib.auth.hashers.Argon2PasswordHasher",
#     "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
#     "django.contrib.auth.hashers.BCryptPasswordHasher",
#     "django.contrib.auth.hashers.PBKDF2PasswordHasher",
#     "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
# ]
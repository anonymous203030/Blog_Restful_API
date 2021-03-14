import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '^8zln(b3lvgulb@0l2hc3v9(df5t6v3s534&^mm^e!$1%_x)0u'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # new!
    'posts',
    'users',
    'todo.backend.todos',
    # 3-rd party
    'rest_framework',
    'drf_yasg',
    'django_filters',
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

ROOT_URLCONF = 'src.urls'

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
# new !
WSGI_APPLICATION = 'src.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

AUTH_USER_MODEL = "users.User"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'users_db': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dee41dc7ts59ga',
        'USER': 'djlbldcxpzonpy',
        'PASSWORD': '27cef3a06ca260dac3ebb5f2d75bb471ce9ed29ec914a5ea08b116c9365bd5c5',
        'HOST': 'ec2-46-137-84-140.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}
# 1dc710c73f90ae85ee61b51c6f5e4bba39bbad75242a203d50bc2388e98418bf
# psql --dbname=d61nc0nbgsq65g --host=ec2-46-137-123-136.eu-west-1.compute.amazonaws.com --port=5432 -U yjqydwjrjcmydr -W

DATABASE_ROUTERS = ['src.routers.AuthRouter', 'src.routers.PrimaryReplicaRouter']

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
# new!


REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 5,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],

}
# AUTH_USER_MODEL = "user_data.User"

LOGIN_URL = 'admin/login/'
LOGOUT_URL = 'admin/logout/'

# CELERY INTEGRATION
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

from pathlib import Path
from decouple import config
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ["*", "http://localhost:5173/", "http://127.0.0.1:5500/"]



INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "storages",
    "users",
    "posts",
    "categorie",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = "core.wsgi.application"
# ASGI_APPLICATION = "core.asgi.application"

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = (
    *default_headers,
    "cache-control",
)

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5500",
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASS'),
        'HOST': config('DATABASE_HOST'),
        'PORT': '5432',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

AUTH_USER_MODEL = "users.User"

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_ROOT = os.path.join(BASE_DIR, config("MEDIA_ROOT"))
MEDIA_URL = config("MEDIA_URL")

USE_S3=config("USE_S3", cast=bool)

if USE_S3:
    AWS_ACCESS_KEY_ID = config("S3_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("S3_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = config("S3_BUCKET_NAME")
    AWS_S3_REGION_NAME = config("S3_REGION_NAME")
    AWS_S3_SIGNATURE_NAME = 's3v4'
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_VERITY = True
    # AWS_S3_ENDPOINT_URL = config("S3_HOST")
    PUBLIC_MEDIA_LOCATION = 'media'
    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'watsapp_backend.storage_backend.StaticStorage'
    AWS_S3_CUSTOM_DOMAIN = f's3.{AWS_S3_REGION_NAME}.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}'
    # MEDIA_URL = f"{AWS_S3_ENDPOINT_URL}{PUBLIC_MEDIA_LOCATION}/"
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    DEFAULT_FILE_STORAGE = "watsapp_backend.storage_backend.PublicMediaStorage"
    
    PRIVATE_MEDIA_LOCATION = 'private'
    PRIVATE_FILE_STORAGE = 'watsapp_backend.storage_backend.PrivateMediaStorage'
else:
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
    MEDIA_ROOT = os.path.join(BASE_DIR, config("MEDIA_ROOT"))
    MEDIA_URL = config("MEDIA_URL")

CELERY_BROKER_URL = 'redis://localhost:6379/0'


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_CACHE_BACKEND': 'django_redis.cache.RedisCache',
}
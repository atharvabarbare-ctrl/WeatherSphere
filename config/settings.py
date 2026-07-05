"""
Django settings for config project.
"""

from pathlib import Path
from decouple import config

# ==========================================
# BASE DIRECTORY
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================
# SECURITY
# ==========================================

SECRET_KEY = config("SECRET_KEY")

# Local Development
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# ==========================================
# APPLICATIONS
# ==========================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'weather',
]


# ==========================================
# MIDDLEWARE
# ==========================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==========================================
# URLS
# ==========================================

ROOT_URLCONF = 'config.urls'


# ==========================================
# TEMPLATES
# ==========================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ==========================================
# WSGI
# ==========================================

WSGI_APPLICATION = 'config.wsgi.application'


# ==========================================
# DATABASE
# ==========================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==========================================
# PASSWORD VALIDATION
# ==========================================

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


# ==========================================
# INTERNATIONALIZATION
# ==========================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# ==========================================
# STATIC FILES
# ==========================================

STATIC_URL = "static/"

# collectstatic command yahan files copy karega
STATIC_ROOT = BASE_DIR / "staticfiles"


# ==========================================
# DEFAULT PRIMARY KEY
# ==========================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ==========================================
# BASIC SECURITY
# ==========================================

X_FRAME_OPTIONS = "DENY"

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True

CSRF_COOKIE_HTTPONLY = True

SESSION_COOKIE_HTTPONLY = True
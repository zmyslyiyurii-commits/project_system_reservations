import os
from pathlib import Path

# Побудова шляхів усередині проекту
BASE_DIR = Path(__file__).resolve().parent.parent

# Швидкі налаштування розробки
SECRET_KEY = 'django-insecure-your-secret-key-here' # У реальному проекті тримай це в таємниці
DEBUG = True
ALLOWED_HOSTS = []

# Реєстрація додатків
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Твій головний додаток
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

ROOT_URLCONF = 'booking_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Шлях до глобальних шаблонів
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

WSGI_APPLICATION = 'booking_system.wsgi.application'

# База даних (SQLite за замовчуванням для розробки)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валідація паролів
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Локалізація
LANGUAGE_CODE = 'uk' # Встановлюємо українську мову
TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_TZ = True

# Статичні файли (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Медіа файли (Завантажені фото кімнат)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Налаштування авторизації (Урок 3)
LOGIN_REDIRECT_URL = 'room_list'  # Куди йдемо після входу
LOGOUT_REDIRECT_URL = 'room_list' # Куди йдемо після виходу

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
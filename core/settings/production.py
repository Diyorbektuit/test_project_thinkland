from .base import *

REST_FRAMEWORK.update({
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
})

DEBUG = False
ALLOWED_HOSTS = ["*"]

# CSRF and CORS
CSRF_TRUSTED_ORIGINS = [
    "https://api-inextlynk.upgrow.uz",
    "https://api.inexlynk.com",
    "https://www.api.inexlynk.com"
]

CORS_ALLOW_HEADERS = [
    "authorization",
    "content-type",
    "x-csrftoken",
    "accept",
    "origin",
    "user-agent",
]

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "PATCH",
    "OPTIONS",
]

CORS_ALLOWED_ORIGINS = [
    "https://api-inextlynk.upgrow.uz",
    "http://localhost:3000",
    "http://localhost:3001",
    "https://upgrow-i-nex-lynk.vercel.app",
    "https://inexlynk.com"
]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = False
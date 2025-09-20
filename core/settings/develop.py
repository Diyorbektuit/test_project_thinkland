from .base import *

ALLOWED_HOSTS = ["*"]
DEBUG = True


# CORS
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "https://api-inextlynk.upgrow.uz",
    "http://localhost:3000",
    "http://localhost:3001",
    "https://upgrow-i-nex-lynk.vercel.app",
    "https://inexlynk.com"
]

# CSRF
CSRF_TRUSTED_ORIGINS = [
    "https://api-inextlynk.upgrow.uz",
    "https://api.inexlynk.com",
    "https://www.api.inexlynk.com"
]
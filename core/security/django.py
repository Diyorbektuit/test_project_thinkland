import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(f"{BASE_DIR}/envs/.env.django")


class DjangoSecurity:
    DJANGO_SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE', "core.settings.develop.txt")
    DJANGO_SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', "some_secret_key")


django_security = DjangoSecurity()


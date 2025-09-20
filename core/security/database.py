import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(f"{BASE_DIR}/envs/.env.database")


class DatabaseSecurity:
    ENGINE = os.environ.get('DB_ENGINE', "django.db.backends.postgresql")
    NAME = os.environ.get('DB_NAME', "some_name")
    USER = os.environ.get('DB_USER', "some_user")
    PASSWORD = os.environ.get('DB_PASSWORD', "some_password")
    HOST = os.environ.get('DB_HOST', "some_host")
    PORT = os.environ.get('DB_PORT', 5432)

database_security = DatabaseSecurity()


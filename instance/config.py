# instance/config.py
import os

SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Untuk SQLite
SQLALCHEMY_TRACK_MODIFICATIONS = False


# Konfigurasi lain
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')

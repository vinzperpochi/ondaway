import os
from datetime import timedelta

class Config:
    # FIX: Use a strong, stable SECRET_KEY so Flask sessions are signed consistently.
    # In production, set this via an environment variable.
    SECRET_KEY = os.environ.get('SECRET_KEY', 'ondajob_super_secret_key_2024_!@#XYZ')

    DB_HOST     = os.environ.get('DB_HOST', 'localhost')
    DB_USER     = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')   # XAMPP default
    DB_NAME     = os.environ.get('DB_NAME', 'job_portal_db')

    # Session config — keep cookies working across the multi-step redirect
    SESSION_PERMANENT        = False
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    SESSION_COOKIE_SECURE    = False   # set True in production (HTTPS)
    SESSION_COOKIE_HTTPONLY  = True
    SESSION_COOKIE_SAMESITE  = 'Lax'

    # Flask-Mail (configure with your SMTP)
    MAIL_SERVER        = 'smtp.gmail.com'
    MAIL_PORT          = 587
    MAIL_USE_TLS       = True
    MAIL_USERNAME      = os.environ.get('MAIL_USERNAME', 'your_email@gmail.com')
    MAIL_PASSWORD      = os.environ.get('MAIL_PASSWORD', 'your_app_password')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME', 'noreply@jobportal.com')
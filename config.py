import os
from decouple import config, Csv
from icecream import ic

# Construct the full absolute path to the .env file
env_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.env'))

# Check if it exists before loading
if not os.path.exists(env_file_path):
    ic(f"File not found: {env_file_path}")
    ic('.env fayli topilmadi!')
    ic('.env.example faylidan nusxa ko\'chirib shablonni o\'zizga moslang.')
    exit(1)

# Use environment variables
SECRET_KEY = config('SECRET_KEY', default='djangorestframework')
DEBUG = config('DEBUG', default=True, cast=bool)
ADMIN_URL = config('ADMIN_URL', default='admin/')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='http://127.0.0.1', cast=Csv())
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='http://127.0.0.1', cast=Csv())
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
API_V1_URL = config('API_V1_URL', default='')
ACCESS_TOKEN_LIFETIME = config('ACCESS_TOKEN_LIFETIME', default=5, cast=int)
REFRESH_TOKEN_LIFETIME = config('REFRESH_TOKEN_LIFETIME', default=1, cast=int)

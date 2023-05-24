from .base import * # noqa 
from .base import env
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KET",
                 default="BEG3czO5iJg_fuicIwFFsuCDJcGblBC2S6vjH3h9UrbZblvF0Lc",
                 )

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
import os

IS_PRODUCTION = os.environ.get('IS_PRODUCTION')

if IS_PRODUCTION:
    from .conf.production.settings import *
else:
    from .conf.development.settings import *

ALLOWED_HOSTS = ['eb-django-app-dev.elasticbeanstalk.com','127.0.0.1']
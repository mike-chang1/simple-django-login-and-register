import os

IS_PRODUCTION = os.environ.get('IS_PRODUCTION')

if IS_PRODUCTION:
    from .conf.production.settings import *
else:
    from .conf.development.settings import *

ALLOWED_HOSTS = ['e3-env.eba-5dwgj7av.us-west-2.elasticbeanstalk.com','127.0.0.1','34.214.242.169','my.econa.net']
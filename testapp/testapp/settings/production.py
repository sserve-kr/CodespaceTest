from .base import *

DEBUG = False

ALLOWED_HOSTS = ['codespacetest.herokuapp.com', '127.0.0.1']

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
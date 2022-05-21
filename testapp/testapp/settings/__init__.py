from .base import *
import os

if os.environ.get('ENV_NAME') == 'STAGE':
    print('Develop Level')
    from .stage import *
elif os.environ.get('ENV_NAME') == 'PRODUCTION':
    print('Production Level')
    from .production import *
else:
    print(os.environ.get('ENV_NAME'))
    print('Local Level (Develop Level Mode)')
    from .stage import *
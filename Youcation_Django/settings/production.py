from Youcation_Django.util import get_server_info_value
from .base import *

SETTING_PRD_DIC = get_server_info_value("production")
SECRET_KEY = SETTING_PRD_DIC["SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = [
    '*'
]

# JWT Token
JWT_AUTH['JWT_SECRET_KEY'] = SETTING_PRD_DIC["SECRET_KEY"]
JWT_AUTH['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'

DATABASES = {
    'default': SETTING_PRD_DIC['DATABASES']['default']
}
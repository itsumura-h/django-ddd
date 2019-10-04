import logging
# import environ

from orator import DatabaseManager
from orator import Model
from django.conf import settings


# env = environ.Env()

# config = {
#     'default': 'database',
#     'database': {
#         'driver': 'postgres',
#         'host': settings.DATABASES['default']['HOST'],
#         'database': settings.DATABASES['default']['NAME'],
#         'port': settings.DATABASES['default']['PORT'],
#         'user': settings.DATABASES['default']['USER'],
#         'password': settings.DATABASES['default']['PASSWORD'],
#         'log_queries': True,
#     }
# }
config = {
    'default': 'database',
    'database': {
        'driver': 'sqlite',
        'database': settings.DATABASES['default']['NAME'],
        'log_queries': True,
    }
}


db = DatabaseManager(config)
Model.set_connection_resolver(db)


logger = logging.getLogger('orator.connection.queries')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    'It took %(elapsed_time)sms to execute the query %(query)s'
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger.addHandler(handler)

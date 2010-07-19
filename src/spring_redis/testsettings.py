import logging

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/tmp/spring_redis.db'
INSTALLED_APPS = ['spring_redis']
ROOT_URLCONF = ['spring_redis.urls']

LOG_FILENAME='test_spring_redis.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)


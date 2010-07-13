from springpython.config import PythonConfig
from springpython.config import Object

from redis.client import Redis


class RedisAppConfig(PythonConfig):
    """
    A SpringPython configuration for wrapping a redis client
    """
    def __init__(self):
        super(RedisAppConfig, self).__init__()

    @Object
    def redis_service(self):
        return Redis()

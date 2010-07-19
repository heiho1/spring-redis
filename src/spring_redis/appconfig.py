from springpython.aop import RegexpMethodPointcutAdvisor, ProxyFactoryObject
from springpython.config import PythonConfig
from springpython.config import Object
from redis.client import Redis

from spring_redis.interceptors import PerformanceInterceptor

REDIS_PATTERNS = [".*select.*", ".*save.*", ".*dbsize.*", ".*delete.*",
    ".*flush.*", ".*append.*", ".*decr.*", ".*exists.*", ".*expire.*",
    ".*get.*", ".*getset.*", ".*incr.*", ".*keys.*", ".*set.*", ]


class RedisAppConfig(PythonConfig):
    """
    A SpringPython configuration for wrapping a redis client
    """
    def __init__(self):
        super(RedisAppConfig, self).__init__()

    @Object
    def perf_advisor(self):
        return RegexpMethodPointcutAdvisor(advice=[PerformanceInterceptor()],
            patterns=REDIS_PATTERNS)

    @Object
    def redis_service(self):
        return ProxyFactoryObject(target=Redis(),
            interceptors=[self.perf_advisor()])

    def after_properties_set(self):
        return True

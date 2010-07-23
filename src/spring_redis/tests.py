import threading
import time
from django.test import TestCase
from springpython.context import ApplicationContext
from spring_redis.appconfig import RedisAppConfig


class SpringRedisTest(TestCase):
    def test_environment(self):
        """Ensures the test runner itself completes successfully"""
        self.assert_(True)

    def test_container(self):
        """
        Validates that the redis service is accessible and functioning
        """
        appctx = ApplicationContext(RedisAppConfig())
        rdssvc = appctx.get_object('redis_service')
        tstky = 'foo'
        tstval = 'bar'
        self.assertTrue(rdssvc.set(tstky, tstval))
        self.assertEquals(rdssvc.get(tstky), tstval)
        self.assertTrue(rdssvc.delete(tstky))
        self.assertFalse(rdssvc.exists(tstky))


from django.test import TestCase

class SpringRedisTest(TestCase):
    def test_environment(self):
        """Ensures the test runner itself completes successfully"""
        self.assert_(True)

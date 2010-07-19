import time
import logging
from springpython.aop import MethodInterceptor


class PerformanceInterceptor(MethodInterceptor):
    """
    Used to profile the time consumed by function invocations
    """
    def invoke(self, invocation):
        start = time.time()
        results = invocation.proceed()
        stop = time.time()
        logging.debug("Invocation:%s: took %2f seconds" % (invocation, \
                      stop - start))

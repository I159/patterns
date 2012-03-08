# !/usr/bin/env python
# -*- coding:utf8 -*-

from time import time


def timer(f):
    def wrap(*args, **kwargs):
        t = time()
        result = f(*args, **kwargs)
        print "Run-time function: %f" % (time()-t)
        return result
    return wrap


# As class
class Timer(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        t = time()
        result = self.f(*args, **kwargs)
        print "Run-time function: %f" % (time()-t)
        return result


# With arguments
def replacer(p=None, a=None):
    def _mid(f):
        class Wrap(object):
            def __init__(self, f, p, a):
                self.f = f
                self.p = p
                self.a = a
            def __call__(self, *args, **kwargs):
                return self.f().replace(p, a)
        return Wrap(f, p, a)
    return _mid

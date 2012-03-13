# !/usr/bin/env python
# -*- coding:utf8 -*-

"""
Attach additional responsibilities to an object dynamically keeping the same
interface. Decorators provide a flexible alternative to subclassing for
extending functionality.
Decorator - one of the most native Python idioms.
"""

from time import time


def timer(f):
    """
    Simple decorator.
    """
    def wrap(*args, **kwargs):
        t = time()
        result = f(*args, **kwargs)
        print "Run-time function: %f" % (time()-t)
        return result
    return wrap


class Timer(object):
    """
    Decorator as class.
    """
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        t = time()
        result = self.f(*args, **kwargs)
        print "Run-time function: %f" % (time()-t)
        return result


def replacer(p=None, a=None):
    """
    Decorator takes extra arguments.
    """
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

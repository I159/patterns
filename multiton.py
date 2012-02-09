#!/usr/bin/env python

"""
Multiton pattern. If any class instance exists, returns existing instance.
"""

def multiton(cls):
    """
    instances should be stored, for real control of existing instances.
    """
    instances = {}
    def classwrapper(*args, **kwargs):
        """
        If in the stored instances have no passed instances it will be created.
        Other way wouldn't be.
        """
        if cls.__name__ not in instances:
            instances[cls.__name__] = cls(*args, **kwargs)
        return instances[cls.__name__]
    return classwrapper


@multiton
class MyClass(object):

    def __init__(self, first=None, second=None):
        assert(first is not None)
        assert(second is not None)





a = MyClass('first', 'second')
b = MyClass('first', 'second')

print a, b

print a is b

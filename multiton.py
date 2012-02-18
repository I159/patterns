#!/usr/bin/env python
# -*- coding; utf-8 -*-

"""
Multiton pattern. If any class instance exists, returns existing instance.
"""

def multiton(cls):
    #TODO: set up mongo for this pattern
    """
    instances should be stored, for real control of existing instances.
    """
    instances = {}
    def classwrapper(*args, **kwargs):
        """
        If in the stored instances have no passed instances it will be created.
        Other way wouldn't be.
        """
        name = '{0}_{1}'.format('_'.join((str(i) for i in args)), cls.__name__)
        if cls.__name__ not in instances:
            print 'not in instances'
            instances[name] = cls(*args, **kwargs)
        return instances[name]
    return classwrapper


@multiton
class MyClass(object):

    def __init__(self, first=None, second=None):
        assert(first is not None)
        assert(second is not None)





a = MyClass('first', 'second')
b = MyClass('first', 'second')
c = MyClass(1, 2)

print 'All instances', a, b, c

print 'a is b', a is b

print 'a is c', a is c

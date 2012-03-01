#!/usr/bin/env python
# -*- coding; utf-8 -*-

"""
Multiton pattern. If any class instance exists, returns existing instance.
"""

def multiton(cls):
    instances = {}

    def classwrapper(*args, **kwargs):
        """
        If in the stored instances have no passed instances it will be created.
        Other way wouldn't be.
        """
        print cls.__name__
        name = '{0}_{1}'.format('_'.join((str(i) for i in args)), cls.__name__)
        if name not in instances:
            print 'not in instances'
            instances[name] = cls(*args, **kwargs)
        return instances.get(name)
    return classwrapper


@multiton
class ClassA(object):

    def __init__(self, first=None, second=None):
        assert(first is not None)
        assert(second is not None)


@multiton
class ClassB(object):

    def __init__(self, first=None, second=None):
        assert(first is not None)
        assert(second is not None)

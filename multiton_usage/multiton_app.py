#!/usr/bin/env python
# -*- coding; utf-8 -*-

from multiton import multiton



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



a = ClassA('one', 'two')
b = ClassB('one', 'two')
c = ClassA('three', 'four')
d = ClassB('one', 'two')

print a is b
print a is c
print b is d
print a, b, c, d

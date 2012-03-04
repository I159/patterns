#!/usr/env/python python
# -*-coding:utf8-*-

from singleton import Singleton


class NewClass(object):
    __metaclass__ = Singleton



a = NewClass()
a.attr = 12
b = NewClass()
print b.attr
print a is b

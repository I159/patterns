# !/usr/env/python python
# -*-coding:utf8-*-

from singleton import Singleton, singleton, SD


class NewClass(object):
    __metaclass__ = Singleton

    def __init__(self):
        print 'Created by Singleton __metaclass__ self', self

    @classmethod
    def cls_meth(cls):
        print 'Created by Singleton __metaclass__ cls', cls


# You can't inherit from this class, because it is not even class befor You
# call it.
@singleton
class AnotherNewClass(object):
    def __init__(self):
        print 'Decorated by singleton decorator self', self

    @classmethod
    def cls_meth(cls):
        print 'Decorated by singleton decorator  cls', cls



@SD
class OneMoreClass(object):
    def __init__(self):
        print self

    @classmethod
    def cls_meth(cls):
        print cls.__name__


def test_one_more_class():
    print 'call', OneMoreClass()
    print 'name: ', OneMoreClass.__name__
    print 'classmethod', OneMoreClass.cls_meth



def instance_creation():
    print '------------------ Metaclass instance comparison -----------------'
    a = NewClass()
    a.attr = 12
    b = NewClass()
    print 'a.attr:', a.attr, 'b.attr', b.attr
    print 'a is b', a is b

    print '------------------ Decorated instance comparison -----------------'
    a = AnotherNewClass()
    a.attr = 12
    b = AnotherNewClass()
    print 'a.attr:', a.attr, 'b.attr', b.attr
    print 'a is b', a is b

def check_types():
    print '---------------------- type of NewClass --------------------------'
    print type(NewClass)
    print '------------------ type of AnotherNewClass -----------------------'
    print type(AnotherNewClass)
    print '------------------ type of NewClass instance ---------------------'
    print type(NewClass())
    print '--------------- type of AnotherNewClass instance -----------------'
    print type(AnotherNewClass())
    print '----------------------- NewClass classmethod ---------------------'
    print NewClass.cls_meth()
    print '-------------------- AnotherNewClass classmethod -----------------'
    print AnotherNewClass.cls_meth()

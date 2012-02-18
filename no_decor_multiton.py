#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Multiton(object):
    def __init__(self):
        self.instances = {}

    def __call__(self, key, instance):
        self.instances['{0}_{1}'.format(instance.__name__, key)] = instance
        return instance

    def get_instance(self, key):
        return self.instances[key]


class A(object):
    def __init__(self, *args, **kwargs):
        def __init(self, *args, **kwargs):
            pass

class B(A):
    pass


m = Multiton()
a = m('a', A())
b = m('b', A())
c = m('b', B())

print 'm.get_instance("a"): ', m.get_instance('a')
print 'a is b', a is b
print 'b is c', b is c
print 'a, b, c', a, b, c

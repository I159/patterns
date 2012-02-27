#! /usr/bin/env python
# -*- coding: utf-8 -*-

class Multiton(object):
    def __init__(self, instance, key):
        self.key = key
        self.instance = instance
        self.instances = {}

    def __call__(self):
        name = '{0}_{1}'.format(self.instance.__class__.__name__, self.key)
        if name not in self.instances:
            self.instances[name] = self.instance
        return self.instances[name]


class A(object):
    def __init__(self, *args, **kwargs):
        pass

class B(A):
    pass




a = Multiton('a', A())

b = Multiton('b', A())

c = Multiton('a', A())

a() is b()

a() is c()

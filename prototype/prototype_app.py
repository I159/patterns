# !/usr/env/python python
# -*- coding: utf8 -*-

from prototype import Prototype

class A(object):
    CLONED = False

    def __init__(self, *args):
        self.args = args

    def is_cloned(self):
        return self.CLONED


class B(A):
    pass

registered_objs = Prototype()

registered_objs.reg_obj('A', A)
b = registered_objs.clone('A')

print A().is_cloned()
print B().is_cloned()
print B.__name__
print B().ARG

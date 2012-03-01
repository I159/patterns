# !/usr/env/python python
# -*- coding: utf8 -*-

from prototype import Prototype

class A(object):
    CLONED = False

    def __init__(self, *args):
        self.args = args

#    def __new__(self):
#        return 'Class A args: %s' % ', '.join(self.args)

    def is_cloned(self):
        return self.CLONED


class B(A):
    def __new__(self):
        return 'Class B args: %s' % ', '.join(self.args)

registered_objs = Prototype()

registered_objs.reg_obj('A', A)
registered_objs.reg_obj('B', B)
C = registered_objs.clone('A')
D = registered_objs.clone('B')

print A().is_cloned()
print C().is_cloned()

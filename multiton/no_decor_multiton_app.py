# !/usr/bin/env python
# -*- coding: utf-8 -*-

from no_decor_multiton import Multiton


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

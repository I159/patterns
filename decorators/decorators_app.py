# !/usr/bin/env python
# -*- coding:utf8 -*-

from decorators import *

@replacer(p='cute', a='insane')
def squirrels():
    return '1000 cute squirrels on my yard'


@timer
def multiplication(intg):
    res = 0
    for i in range(intg):
        res = res + (intg * i)
    return res


@Timer
def composition(intg):
    res = 0
    for i in range(intg):
        res = res + (intg + i)
    return res



squirrels()
multiplication(3)
composition(3)

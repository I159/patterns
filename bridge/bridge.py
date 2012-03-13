# !/usr/bin/env python
# -*- coding:utf8 -*-
"""
The bridge pattern is a design pattern used in software engineering which
is meant to "decouple an abstraction from its implementation so that the two
can vary independently". The bridge uses encapsulation, aggregation, and can
use inheritance to separate responsibilities into different classes.
"""


class SortImpl(object):
    """
    Interface provides functionality implementation.
    """
    def __init__(self, sort_type):
        self._sort_impl = sort_type

    def sort(self, data):
        self._sort_impl.sort(data)
        return data


class SortAbs(object):
    """
    Abstraction provides functionality.
    """
    def sort(self, data):
        raise NotImplementedError

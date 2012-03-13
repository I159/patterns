# !/usr/bin/env python
# -*- coding:utf8 -*-
"""
Decouple an abstraction from its implementation
"""


class SortImpl(object):
    def __init__(self, sort_type):
        self._sort_impl = sort_type

    def sort(self, data):
        self._sort_impl.sort(data)
        return data


class SortAbs(object):
    def sort(self, data):
        raise NotImplementedError

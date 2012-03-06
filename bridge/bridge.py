# /usr/bin/env python
# -*- coding:utf8 -*-


class SortAbs(object):
    def __init__(self, sort_type):
        self._sort_impl = sort_type

    def sort(self, data):
        self._sort_impl.sort(data)
        return data


class SortImpl(object):
    def sort(self, data):
        raise NotImplementedError

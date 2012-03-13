# !/usr/bin/env python
# -*- coding:utf8 -*-

from bridge import *


class RegSort(SortAbs):
    """
    Appointed abstract method
    Functionality provided via abstraction inheritance.
    """
    def sort(self, data):
        return data.sort()


class RevSort(SortAbs):
    """
    Functionality provided via abstraction inheritance.
    """
    def sort(self, data):
        data.sort()
        data.reverse()
        return data



# Implementation
regular_sorting = SortImpl(RegSort())
reverse_sorting = SortImpl(RevSort())
# Usage
print regular_sorting.sort([3,2,5,1,4])
print reverse_sorting.sort([3,2,5,1,4])

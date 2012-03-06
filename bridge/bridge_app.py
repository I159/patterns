# /usr/bin/env python
# -*- coding:utf8 -*-

from bridge import *


class RegSort(SortImpl):
    def sort(self, data):
        return data.sort()


class RevSort(SortImpl):
    def sort(self, data):
        data.sort()
        data.reverse()
        return data




regular_sorting = SortAbs(RegSort())
reverse_sorting = SortAbs(RevSort())
print regular_sorting.sort([3,2,5,1,4])
print reverse_sorting.sort([3,2,5,1,4])

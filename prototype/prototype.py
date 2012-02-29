# !/usr/env/python python
# -*- coding: utf8 -*-

from copy import deepcopy


class Prototype(object):
    def __init__(self):
        self._objects = {}

    def reg_obj(self, name, obj):
        self._objects[name] = obj

    def unregister_obj(self, name):
        del self._objects[name]

    def clone(self, name):
        obj = deepcopy(self._objects[name])
        obj.CLONED = True
        return obj

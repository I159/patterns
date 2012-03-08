# !/usr/bin/env python
# -*- coding: utf-8 -*-

class Resource(object):
    __value = 0

    def reset(self):
        self.__value = 0

    def set_value(self, val):
        self.__value = val

    def get_value(self):
        return self.__value


class ObjectPool(object):
    __instance = None
    __resources = list()

    def __init__(self):
        if ObjectPool.__instance != None:
            raise NotImplemented("This is a singleton class")

    @staticmethod
    def get_instance():
        if ObjectPool.__instance == None:
            ObjectPool.__instance = ObjectPool()

        return ObjectPool.__instance

    def get_resource(self):
        if len(self.__resources) > 0:
            print "Using  existing resource"
            return self.__resources.pop(0)
        else:
            print "Creating new resource"
            return Resource()

    def set_resource(self, resource):
        self.__resources.append(resource)

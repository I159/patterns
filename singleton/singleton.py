#!/usr/env/python python
# -*-coding:utf8-*-

class Singleton(type):
    def __init__(self, name, bases, dict):
        super(Singleton, self).__init__(name, bases, dict)
        self._instance = None

    def __call__(self):
        if self._instance is None:
            self._instance = super(Singleton, self).__call__()
        return self._instance

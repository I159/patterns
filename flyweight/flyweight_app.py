#!/usr/bin/en python
#-*-coding:utf8-*-

from flyweight import Flyweight

class F(Flyweight):
    def get_value(self):
        return self.value

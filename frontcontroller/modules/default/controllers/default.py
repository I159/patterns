# !/usr/bin/env python
# -*-coding: utf8 -*-

class Instance(object):
    def __init__(self, instance):
        self.instance = instance

    def default_action(self):
        return self.instance.__class__.__name__

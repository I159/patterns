# !/usr/bin/env python
# -*- coding: utf8 -*-
"""
 Adapter pattern is used to convert the interface of an object to one the
 client expects, allowing collaboration between classes that normally couldn't
 work together due to differing interfaces.
"""

class ParamAdapter(object):
    """
    Adapter with parameter
    """
    def __init__(self, pat):
        self.pat = pat

    def make_noise(self):
        return self.pat.noise()

    def __getattr__(self, attr):
        return getattr(self.pat, attr)


class AbsAdapter(object):
    """
    Abstract adapter
    """
    def make_noise(self):
        raise NotImplementedError


class Client(object):
    """
    Client, which adapters required
    """
    pat_name = None
    pat_noise = None
    def noise(self):
        return self.pat_noise

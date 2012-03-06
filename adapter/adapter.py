# /usr/env/python python
# -*- coding: utf8 -*-

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
    def make_noise(self):
        raise NotImplementedError


class Client(object):
    pat_name = None
    pat_noise = None
    def noise(self):
        return self.pat_noise

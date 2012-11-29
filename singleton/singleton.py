# !/usr/env/python python
# -*-coding:utf8-*-

class Singleton(type):
    """ Meta class singleton pattern.
    should be used as ::__metaclass__ = Singleton
    """
    def __init__(self, name, bases, dict):
        super(Singleton, self).__init__(name, bases, dict)
        self._instance = None

    def __call__(self):
        if self._instance is None:
            self._instance = super(Singleton, self).__call__()
        return self._instance


def singleton(cls):
    inst = {}
    def get(*args, **kwargs):
        cls_id = id(cls)
        if cls_id not in inst:
            inst[cls_id] = cls(*args, **kwargs)
        return inst[cls_id]
    return get


class SingletonDecorator(object):
    inst = {}
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        cls_id = id(self.cls)
        if cls_id not in self.inst:
            self.inst[cls_id] = self.cls(*args, **kwargs)
        return self.inst[cls_id]


class SD(object):
    """ The right way to decorate classes """
    inst = {}
    def __init__(self, cls):
        self.__dict__.update(cls.__dict__)
        self.__name__ = cls.__name__
        self.cls = cls

    def __call__(self, *args, **kwargs):
        if self.cls not in self.inst:
            self.inst[self.cls] = self.cls(*args, **kwargs)
        return self.inst[self.cls]


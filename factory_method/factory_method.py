#!/usr/bin/env python
# -*- coding; utf-8 -*-
"""
Define an interface for creating an object, but let subclasses decide which
class to instantiate. Factory Method lets a class defer instantiation to
subclasses
"""


class Culture(object):
    """
    Base class for main content processing.
    """
    def get_culture(self):
        return self.__str__()



class Goverment(object):
    """
    Base structure class.
    """
    def __str__(self):
        return self.culture.__str__()

    def get_culture(self):
        return self.culture.get_culture()

    def set_culture(self):
        """
        Abstract method. Required self.culture attribute as
        Culture class instance.
        """
        raise NotImplementedError

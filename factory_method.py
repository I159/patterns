#!/usr/bin/env python
# -*- coding; utf-8 -*-

class Culture(object):
    """
    Base class for main content processing.
    """
    def get_culture(self):
        return self.__str__()


class Democracy(Culture):
    def __str__(self):
        return 'Democracy'


class Dictature(Culture):
    def __str__(self):
        return 'Dictature'


class Goverment(object):
    """
    Base structure class.
    """
    def __str__(self):
        return self.culture.__str__()

    def get_culture(self):
        return self.culture.get_culture()

    def set_culture(self):
        raise NotImplementedError


class GovermentA(Goverment):
    def set_culture(self):
        self.culture = Democracy()


class GovermentB(Goverment):
    def set_culture(self):
        self.culture = Dictature()


g1 = GovermentA()
g1.set_culture()
print str(g1)

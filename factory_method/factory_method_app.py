#!/usr/bin/env python
# -*- coding; utf-8 -*-

import factory_method

class Dictature(factory_method.Culture):
    """
    Defined __str__ as abstraction method.
    """
    def __str__(self):
        return 'Dictature'


class GovermentA(factory_method.Goverment):
    """
    Defined abs method implements main functionality.
    """
    def set_culture(self):
        self.culture = Dictature()


g1 = GovermentA()
# By calling get_culture method implemented main functionality to abstraction
g1.set_culture()
print str(g1)



